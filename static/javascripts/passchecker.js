// document.addEventListener("DOMContentLoaded", function () {
//     const form = document.getElementById("pdf-form");

//     form.addEventListener("submit", function (e) {
//         const password = document.getElementById('password').value;
//         const confirmPassword = document.getElementById('confirmPassword').value;
//         const message = document.getElementById('message');

//         message.innerHTML = ''; // Clear previous message

//         if (password.length < 8) {
//             message.innerHTML = 'Password must be at least 8 characters long';
//             message.style.color = 'red';
//             e.preventDefault(); // Stop form submission
//             return;
//         }

//         if (password !== confirmPassword) {
//             message.innerHTML = 'Passwords do not match';
//             message.style.color = 'red';
//             e.preventDefault(); // Stop form submission
//             return;
//         }

//         message.innerHTML = 'Passwords match';
//         message.style.color = 'green';

//         // Form can now be submitted
//     });
// });
// // This script checks the password and confirm password fields when the form is submitted.

document.addEventListener("DOMContentLoaded", function () {
    // Password toggle functionality
    const togglePassword = document.getElementById('toggle-password');
    const passwordField = document.getElementById('password');

    const toggleConfirmPassword = document.getElementById('toggle-confirm-password');
    const confirmPasswordField = document.getElementById('confirmPassword');

    togglePassword.addEventListener('click', function () {
        // Toggle the type between password and text
        if (passwordField.type === "password") {
            passwordField.type = "text";
            togglePassword.innerHTML = '<i class="fa-solid fa-eye-slash"></i>'; // Change button text to "Hide"
        } else {
            passwordField.type = "password";
            togglePassword.innerHTML = '<i class="fa-solid fa-eye"></i>'; // Change button text to "Show"
        }
    });

    toggleConfirmPassword.addEventListener('click', function () {
        // Toggle the type between password and text
        if (confirmPasswordField.type === "password") {
            confirmPasswordField.type = "text";
            toggleConfirmPassword.innerHTML = '<i class="fa-solid fa-eye-slash"></i>'; // Change button text to "Hide"
        } else {
            confirmPasswordField.type = "password";
            toggleConfirmPassword.innerHTML = '<i class="fa-solid fa-eye"></i>'; // Change button text to "Show"
        }
    });

    // Form submit handling and password validation
    const form = document.getElementById("pdf-form");

    form.addEventListener("submit", function (e) {
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        const message = document.getElementById('message');

        message.innerHTML = ''; // Clear previous message

        if (password.length < 8) {
            message.innerHTML = 'Password must be at least 8 characters long';
            message.style.color = 'red';
            e.preventDefault(); // Stop form submission
            return;
        }

        if (password !== confirmPassword) {
            message.innerHTML = 'Passwords do not match';
            message.style.color = 'red';
            e.preventDefault(); // Stop form submission
            return;
        }

        message.innerHTML = 'Passwords match';
        message.style.color = 'green';

        // Form can now be submitted
    });
});
