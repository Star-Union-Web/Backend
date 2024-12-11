  // Check password strength (basic example)
  if (passwordInput.value.length < 8) {
    alert('Password must be at least 8 characters long');
    return;
}

const newUser = {
    username: usernameInput.value,
    email: emailInput.value,
    password: passwordInput.value
};

// In a real application, you would send this to a backend
users.push(newUser);

console.log('New user registered:', newUser);

// Redirect to login page or show success message
alert('Registration successful! Please login.');
window.location.href = 'login.html';;
;