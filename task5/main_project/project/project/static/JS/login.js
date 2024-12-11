const email = emailInput.value;
const password = passwordInput.value;

// Simple login validation
const user = users.find(u => u.email === email && u.password === password);

if (user) {
    // Successful login
    alert('Login successful!');
    // Redirect to homepage or dashboard
    window.location.href = 'index.html';
} else {
    // Failed login
    alert('Invalid email or password');
}
;

forgotPasswordLink.addEventListener('click', (e) => {
e.preventDefault();
alert('Password reset functionality not implemented in this demo.');
});
;