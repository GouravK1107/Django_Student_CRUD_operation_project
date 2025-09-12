// Wait until page is loaded
window.onload = function () {
    const form = document.querySelector("form");

    form.onsubmit = function (event) {
        let email = document.querySelector("input[name='user_email']").value.trim();
        let password = document.querySelector("input[name='user_password']").value.trim();
        let phone = document.querySelector("input[name='user_phone_number']").value.trim();

        if (email === "" || password === "" || phone === "") {
            alert("⚠️ Please fill in all fields before submitting.");
            event.preventDefault(); // Stop form submission
        } else {
            alert("✅ Form submitted successfully!");
        }
    };
};
