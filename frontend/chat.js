/**
 * Conversational Chat Interface for EquityBridge
 * Collects organization info through guided conversation
 */

const API_URL = window.API_URL || 'https://ideal-flow-production-2795.up.railway.app';

// Conversation state
let currentStep = 0;
let userData = {
    name: '',
    zip_code: '',
    mission: '',
    focus_area: '',
    annual_budget: 0,
    staff_size: '',
    county: null
};

// Conversation flow
const conversation = [
    {
        step: 0,
        bot: "Hi! I'm EquityBridge, your grant advisor. What's your organization's name?",
        field: 'name',
        validate: (val) => val.trim().length > 0,
        error: "Please enter your organization's name."
    },
    {
        step: 1,
        bot: "Great! What's your zip code?",
        field: 'zip_code',
        validate: (val) => /^\d{5}$/.test(val.trim()),
        error: "Please enter a valid 5-digit zip code.",
        transform: (val) => val.trim()
    },
    {
        step: 2,
        bot: "Tell me about your organization's mission. What kind of work do you do?",
        field: 'mission',
        validate: (val) => val.trim().length > 10,
        error: "Please tell us more about your mission (at least 10 characters).",
        extractFocus: true // Extract focus area from mission
    },
    {
        step: 3,
        bot: "What's your approximate annual budget? (Just the number, like 250000)",
        field: 'annual_budget',
        validate: (val) => {
            const num = parseInt(val.replace(/[^0-9]/g, ''));
            return !isNaN(num) && num > 0;
        },
        error: "Please enter a valid budget amount.",
        transform: (val) => {
            // Handle formats like "$250,000", "250K", "250000"
            let cleaned = val.replace(/[^0-9kK]/g, '');
            if (cleaned.toLowerCase().includes('k')) {
                return parseInt(cleaned.replace(/[^0-9]/g, '')) * 1000;
            }
            return parseInt(cleaned) || 0;
        }
    },
    {
        step: 4,
        bot: "How many staff members do you have? (Type '1-5', '6-20', '21-50', or '50+')",
        field: 'staff_size',
        validate: (val) => {
            const normalized = val.trim().toLowerCase();
            return ['1-5', '6-20', '21-50', '50+'].includes(normalized) ||
                   ['1', '2', '3', '4', '5'].includes(normalized) ||
                   (parseInt(normalized) >= 1);
        },
        error: "Please enter a valid staff size (1-5, 6-20, 21-50, or 50+).",
        transform: (val) => {
            const normalized = val.trim();
            const num = parseInt(normalized);
            if (!isNaN(num)) {
                if (num <= 5) return '1-5';
                if (num <= 20) return '6-20';
                if (num <= 50) return '21-50';
                return '50+';
            }
            return normalized;
        }
    }
];

// Initialize chat
function initChat() {
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const chatSend = document.getElementById('chat-send');
    
    // Show first message
    addBotMessage(conversation[0].bot);
    
    // Handle send button
    chatSend.addEventListener('click', handleUserInput);
    
    // Handle Enter key
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleUserInput();
        }
    });
    
    // Focus input
    chatInput.focus();
}

// Add bot message
function addBotMessage(text) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'chat-message bot-message';
    messageDiv.innerHTML = `<div class="message-content">${escapeHtml(text)}</div>`;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Add user message
function addUserMessage(text) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'chat-message user-message';
    messageDiv.innerHTML = `<div class="message-content">${escapeHtml(text)}</div>`;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Handle user input
function handleUserInput() {
    const chatInput = document.getElementById('chat-input');
    const userText = chatInput.value.trim();
    
    if (!userText) return;
    
    // Add user message
    addUserMessage(userText);
    chatInput.value = '';
    
    // Process current step
    const current = conversation[currentStep];
    let value = userText;
    
    // Transform if needed
    if (current.transform) {
        value = current.transform(userText);
    }
    
    // Validate
    if (!current.validate(value)) {
        addBotMessage(current.error);
        return;
    }
    
    // Store value
    userData[current.field] = value;
    
    // Extract focus area from mission if needed
    if (current.extractFocus && currentStep === 2) {
        userData.focus_area = detectFocusArea(userText);
    }
    
    // Move to next step
    currentStep++;
    
    // Check if we need confirmation
    if (currentStep >= conversation.length) {
        showConfirmation();
    } else {
        // Show next question
        addBotMessage(conversation[currentStep].bot);
    }
}

// Detect focus area from text
function detectFocusArea(text) {
    const lowerText = text.toLowerCase();
    const healthKeywords = ['health', 'medical', 'clinic', 'wellness', 'maternal', 'community health', 'healthcare', 'hospital', 'patient', 'treatment'];
    const envKeywords = ['environment', 'environmental', 'conservation', 'air quality', 'water', 'climate', 'sustainability', 'pollution', 'green', 'renewable'];
    
    const hasHealth = healthKeywords.some(keyword => lowerText.includes(keyword));
    const hasEnv = envKeywords.some(keyword => lowerText.includes(keyword));
    
    if (hasHealth && hasEnv) return 'both';
    if (hasHealth) return 'health';
    if (hasEnv) return 'environment';
    
    // Default to 'both' if unclear
    return 'both';
}

// Show confirmation
function showConfirmation() {
    const focusAreaText = {
        'health': 'Health',
        'environment': 'Environment',
        'both': 'Health & Environment'
    };
    
    const confirmation = `Perfect! Let me confirm what I have:

**Organization:** ${userData.name}
**Location:** ${userData.zip_code}
**Focus Area:** ${focusAreaText[userData.focus_area] || 'Both'}
**Budget:** $${userData.annual_budget.toLocaleString()}
**Staff Size:** ${userData.staff_size}

Does this look correct? (Type 'yes' to continue or 'no' to start over)`;
    
    addBotMessage(confirmation);
    
    // Wait for confirmation
    const chatInput = document.getElementById('chat-input');
    const chatSend = document.getElementById('chat-send');
    
    const confirmHandler = () => {
        const response = chatInput.value.trim().toLowerCase();
        if (response === 'yes' || response === 'y') {
            chatInput.removeEventListener('keypress', confirmKeyHandler);
            chatSend.removeEventListener('click', confirmHandler);
            searchGrants();
        } else if (response === 'no' || response === 'n') {
            chatInput.removeEventListener('keypress', confirmKeyHandler);
            chatSend.removeEventListener('click', confirmHandler);
            resetChat();
        } else {
            addBotMessage("Please type 'yes' to continue or 'no' to start over.");
            chatInput.value = '';
        }
    };
    
    const confirmKeyHandler = (e) => {
        if (e.key === 'Enter') {
            confirmHandler();
        }
    };
    
    chatSend.addEventListener('click', confirmHandler);
    chatInput.addEventListener('keypress', confirmKeyHandler);
}

// Search grants
async function searchGrants() {
    addBotMessage("Great! Let me search for grants that match your organization...");
    
    // Show loading
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'chat-message bot-message';
    loadingDiv.id = 'loading-message';
    loadingDiv.innerHTML = '<div class="message-content">🔍 Searching grants...</div>';
    document.getElementById('chat-messages').appendChild(loadingDiv);
    
    try {
        // Prepare profile data
        const profile = {
            name: userData.name,
            zip_code: userData.zip_code,
            mission: userData.mission,
            focus_area: userData.focus_area,
            annual_budget: userData.annual_budget,
            staff_size: userData.staff_size,
            county: userData.county
        };
        
        // Call API
        const response = await fetch(`${API_URL}/api/match-grants`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(profile)
        });
        
        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Remove loading
        const loadingMsg = document.getElementById('loading-message');
        if (loadingMsg) loadingMsg.remove();
        
        // Display results
        displayGrantResults(data);
        
    } catch (error) {
        console.error('Error:', error);
        const loadingMsg = document.getElementById('loading-message');
        if (loadingMsg) loadingMsg.remove();
        addBotMessage(`Sorry, I encountered an error while searching for grants: ${error.message}. Please try again later.`);
    }
}

// Display grant results
function displayGrantResults(data) {
    if (!data.grants || data.grants.length === 0) {
        addBotMessage("I couldn't find any matching grants. Try adjusting your criteria or contact us for help.");
        return;
    }
    
    let resultsText = `🎉 Great news! I found ${data.matches_found} grant${data.matches_found === 1 ? '' : 's'} that match your organization:\n\n`;
    
    data.grants.forEach((grant, index) => {
        resultsText += `**${index + 1}. ${grant.title}** (${grant.match_score}% match)\n`;
        resultsText += `   💰 Amount: ${grant.amount}\n`;
        resultsText += `   📅 Deadline: ${grant.deadline}\n`;
        resultsText += `   🏢 Funder: ${grant.funder}\n`;
        resultsText += `   ✅ Why it matches: ${grant.match_reason}\n\n`;
    });
    
    resultsText += "Would you like to see these results on a map or get more details?";
    
    addBotMessage(resultsText);
    
    // Also trigger the results display in the main app
    if (window.displayResults) {
        window.displayResults(data);
    }
    
    // Initialize map if available
    if (window.initializeMap && !window.mapInitialized) {
        window.initializeMap();
        window.mapInitialized = true;
    }
    
    // Highlight matching grants on map
    if (window.highlightMatchingGrants && data.grants) {
        window.highlightMatchingGrants(data.grants);
    }
    
    if (window.showUserLocation && userData.zip_code) {
        window.showUserLocation(userData.zip_code);
    }
}

// Reset chat
function resetChat() {
    currentStep = 0;
    userData = {
        name: '',
        zip_code: '',
        mission: '',
        focus_area: '',
        annual_budget: 0,
        staff_size: '',
        county: null
    };
    
    const chatMessages = document.getElementById('chat-messages');
    chatMessages.innerHTML = '';
    
    addBotMessage(conversation[0].bot);
}

// Escape HTML
function escapeHtml(unsafe) {
    if (!unsafe) return '';
    return unsafe
        .toString()
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChat);
} else {
    initChat();
}

