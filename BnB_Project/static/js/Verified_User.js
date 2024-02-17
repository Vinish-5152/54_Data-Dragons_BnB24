// JavaScript function to handle the button click


function new_user(type) {
    console.log('New user type: ' + type);
    console.log('CLICKED');
    fetch(`/user/?user_type=${type}`, {
        method: 'POST', 
        headers: {
            'X-CSRFToken': csrftoken  // Include the CSRF token in the request headers
        } // or 'POST' depending on your implementation
    })
        .then(response => {
            if (!response.ok) {

                throw new Error('Network response was not ok');

            }

            return response.json();
        })
        .then(data => {
            console.log('redirecting')
            window.location.href = '/seller/home'
            console.log('redirected')
            console.log(data);  // log or handle the server response
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        })
}