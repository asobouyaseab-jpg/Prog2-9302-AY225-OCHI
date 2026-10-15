// Get DOM elements
const passwordDisplay = document.getElementById('password');
const lengthInput = document.getElementById('length');
const lengthValue = document.getElementById('lengthValue');
const uppercaseCheckbox = document.getElementById('uppercase');
const lowercaseCheckbox = document.getElementById('lowercase');
const numbersCheckbox = document.getElementById('numbers');
const symbolsCheckbox = document.getElementById('symbols');
const generateBtn = document.getElementById('generateBtn');
const copyBtn = document.getElementById('copyBtn');

// character sets
const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
const numberChars = '0123456789';
const symbolChars = '!@#$%^&*()_+-=[]{}|;:,.<>?';

// Update slider value display
lengthInput.addEventListener('input', () => {
    lengthValue.textContent = lengthInput.value;
});

// Password generation function
function generatePassword() {
    let chars = '';
    if (uppercaseCheckbox.checked) chars += uppercaseChars;
    if (lowercaseCheckbox.checked) chars += lowercaseChars;
    if (numbersCheckbox.checked) chars += numberChars;
    if (symbolsCheckbox.checked) chars += symbolChars;

    // Alert if no character types are selected
    if (!chars) {
        alert('Please select at least one character type！');
        return '';
    }

    const length = parseInt(lengthInput.value);
    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        password += chars[randomIndex];
    }
    return password;
}

// Generate button click event
generateBtn.addEventListener('click', () => {
    const password = generatePassword();
    if (password) {
        passwordDisplay.value = password;
    }
});

// copy button click event
copyBtn.addEventListener('click', () => {
    if (passwordDisplay.value && passwordDisplay.value !== 'Password will appear here') {
        navigator.clipboard.writeText(passwordDisplay.value)
            .then(() => alert('Password copied to clipboard！'))
            .catch(() => alert('Failed to copy password.'));
    }
});

// generate initial password
generateBtn.click();