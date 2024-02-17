// JavaScript function to handle the button click

document.addEventListener('DOMContentLoaded', function () {
    // Your code here
    document.getElementById("email_verify_otp").addEventListener("click", email_verifyOtp);
    document.getElementById("Ph_verify_otp").addEventListener("click", ph_verifyOtp);
    document.getElementById('email_send_otp').addEventListener("click", email_sendOtp);
    document.getElementById('ph_send_otp').addEventListener("click", ph_sendOtp);
    document.getElementById('ph_number').addEventListener("input", ph_updater);
    document.getElementById('email_id').addEventListener("input", email_updater);
});

let email = document.getElementById('email_id').value;
let ph_number = document.getElementById('ph_number').value;
if (email) {
    let report_err = document.getElementById('email_otp_ver_error');
    let report_suc = document.getElementById('email_otp_ver_success');
    let report_ver = document.getElementById('email_otp_valid');
    if (report_ver === true) {
        report_err.innerHTML = '';
        report_suc.innerHTML = "** OTP VERIFIED **";
    } else {
        report_suc.innerHTML = '';
        report_err.innerHTML = '** OTP NOT VERIFIED **';
    }
}

if (ph_number) {
    let otp_ver = document.getElementById('Ph_otp_valid');
    let report_suc = document.getElementById('Ph_otp_ver_success');
    let report_err = document.getElementById('Ph_otp_ver_error');
    if (otp_ver === true) {
        report_err.innerHTML = '';
        report_suc.innerHTML = '** OTP VERIFIED **';
    } else {
        report_suc.innerHTML = '';
        report_err.innerHTML = '** OTP NOT VERIFIED **';
    }
}

function email_sendOtp() {
    console.log('CLICKED')
    let email = document.getElementById('email_id').value;  // Replace with your logic to get the email
    console.log('EMAIL : ', email)
    let otp_ver = document.getElementById('email_otp_valid');
    let report_err = document.getElementById('email_otp_send_error');
    let report_suc = document.getElementById('email_otp_send_success');
    let report_err_ver = document.getElementById('email_otp_ver_error');
    let report_suc_ver = document.getElementById('email_otp_ver_success');
    if (email) {
        // Make an AJAX request to your Django view with the email parameter
        report_err.innerHTML = '';
        report_suc.innerHTML = '** SENDING OTP **';
        otp_ver.checked = false;
        report_suc_ver.innerHTML = '';
        report_err_ver.innerHTML = '';
        fetch(`send_otp_via_email/?email=${email}`, {
            method: 'GET',  // or 'POST' depending on your implementation
        })
            .then(response => {
                if (!response.ok) {
                    report_suc.innerHTML = '';
                    report_err.innerHTML = '** FAILED TO SEND OTP **';

                    throw new Error('Network response was not ok');

                }
                return response.json();
            })
            .then(data => {
                if (data.status === 'error') {
                    report_suc.innerHTML = ''
                    report_err.innerHTML = '** ' + data.message + ' **';
                } else {
                    report_err.innerHTML = ''
                    report_suc.innerHTML = '** ' + data.message + ' **';
                }
                console.log(data);  // log or handle the server response
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            })
    } else {
        let report = document.getElementById('email_otp_send_error');
        report.innerHTML = '** KINDLY ENTER EMAIL ID **';
    }
}


function email_verifyOtp() {
    console.log('CLICKED..')
    let e_otp = document.getElementById('email_otp').value;
    let email = document.getElementById('email_id').value;
    let otp_ver = document.getElementById('email_otp_valid');
    console.log(e_otp)
    let report_err = document.getElementById('email_otp_ver_error');
    let report_suc = document.getElementById('email_otp_ver_success');

    if (otp_ver.checked === true) {
        report_suc.innerHTML = '** OTP ALREADY VERIFIED **';
        report_err.innerHTML = '';
    } else if (e_otp) {
        report_suc.innerHTML = '** VERIFING OTP **';
        report_err.innerHTML = '';
        fetch(`verify_otp_via_email/?email=${email}&e_otp=${e_otp}`, {method: 'GET'})
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.status === 'error') {
                    report_err.innerHTML = '** ' + data.message + ' **';
                    otp_ver.checked = false
                    report_suc.innerHTML = ''
                } else {
                    report_err.innerHTML = ''
                    if (data.message === 'OTP VERIFIED') {
                        otp_ver.checked = true;
                        console.log('OTP VERIFIED');
                    }
                    report_suc.innerHTML = '** ' + data.message + ' **';
                }
                console.log(data);  // log or handle the server response  // log or handle the server response
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            })
    } else {
        report_err.innerHTML = '** KINDLY ENTER OTP TO VERIFY **';
    }
}

function email_updater() {
    let otp_ver = document.getElementById('email_otp_valid');

    console.log(otp_ver.checked);

    let report_err = document.getElementById('email_otp_ver_error');
    let report_suc = document.getElementById('email_otp_ver_success');
    if (otp_ver.checked === true) {
        otp_ver.checked = false;
        report_suc.innerHTML = '';
        report_err.innerHTML = '** OTP NOT VERIFIED (EMAIL ID CHANGED) **';
    }

}


function ph_sendOtp() {
    console.log('PH SEND OTP');
    let num = document.getElementById('ph_number').value;
    let report_suc = document.getElementById('ph_otp_send_success');
    let report_err = document.getElementById('ph_otp_send_error');
    let otp_ver = document.getElementById('Ph_otp_valid');
    let report_suc_ver = document.getElementById('Ph_otp_ver_success');
    let report_err_ver = document.getElementById('Ph_otp_ver_error');
    if (num) {
        console.log('SENDING OTP');
        report_err.innerHTML = '';
        report_suc.innerHTML = '** SENDING OTP **';
        otp_ver.checked = false;
        report_suc_ver.innerHTML = '';
        report_err_ver.innerHTML = '';
        fetch(`send_otp_via_sms/?ph=${num}`, {method: 'GET'})
            .then(response => {
                if (!response.ok) {
                    report_suc.innerHTML = '';
                    report_err.innerHTML = '** FAILED TO SEND OTP **';
                    throw new Error('Network Response Was Not Ok');
                }
                return response.json()
            })
            .then(data => {
                if (data.status === 'success') {
                    report_err.innerHTML = '';
                    report_suc.innerHTML = '** ' + data.message + ' **';
                } else {
                    report_suc.innerHTML = '';
                    report_err.innerHTML = '** ' + data.message + ' **';
                }
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            })
    } else {
        report_suc.innerHTML = '';
        report_err.innerHTML = '** KINDLY ENTER PHONE NUMBER **';
    }
}

function ph_verifyOtp() {
    let num = document.getElementById('ph_number').value;
    let e_otp = document.getElementById('Ph_otp').value;
    let otp_ver = document.getElementById('Ph_otp_valid');
    let report_suc = document.getElementById('Ph_otp_ver_success');
    let report_err = document.getElementById('Ph_otp_ver_error');

    if (otp_ver.checked === true) {
        report_suc.innerHTML = '** PHONE NUMBER ALREADY VERIFIED **';
        report_err.innerHTML = '';
    } else if (e_otp) {
        console.log('VERIFING OTP');
        report_err.innerHTML = ''
        report_suc.innerHTML = '** VERIFING OTP **';
        fetch(`verify_otp_via_sms/?ph=${num}&e_otp=${e_otp}`, {method: 'GET'})
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network Response Was Not Ok');
                }
                return response.json()
            })
            .then(data => {
                if (data.status === 'success') {
                    report_err.innerHTML = '';
                    if (data.message === 'OTP VERIFIED') {
                        otp_ver.checked = true;
                        console.log('OTP VERIFIED');
                    }
                    report_suc.innerHTML = '** ' + data.message + ' **';
                } else {
                    report_suc.innerHTML = '';
                    report_err.innerHTML = '** ' + data.message + ' **';
                }
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            })
    } else {
        report_suc.innerHTML = '';
        report_err.innerHTML = '** KINDLY ENTER OTP TO VERIFY **';
    }
}

function ph_updater() {
    let otp_ver = document.getElementById('Ph_otp_valid');
    let report_suc = document.getElementById('Ph_otp_ver_success');
    let report_err = document.getElementById('Ph_otp_ver_error');

    if (otp_ver.checked === true) {
        otp_ver.checked = false;
        report_suc.innerHTML = '';
        report_err.innerHTML = '** OTP NOT VERIFIED (Phone Number CHANGED) **';
    }
}