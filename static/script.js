'use strict';

let form_being_submitted = false;

const checkForm = function (form) {
	if (form_being_submitted) {
		alert('The form is being submitted, please wait a moment...');
		form.myButton.disabled = true;
		return false;
	}

	const dataArr = [...new FormData(document.querySelector('#rain-form'))];
	const data = Object.fromEntries(dataArr);
	// console.log(data);

	if (
		data.Min_Temp == '' ||
		data.Max_Temp == '' ||
		data.Wind_Direc == '' ||
		data.Wind_Speed == '' ||
		data.Humidity == '' ||
		data.Pressure == '' ||
		data.Cloud == '' ||
		data.Temperature_C == '' ||
		data.Today_Rain == '-- Does it rain today--' ||
		data.location == 'Select Location'
	) {
		alert('please fill the form fields before submitting');
		form.myButton.disabled = false;
		return false;
	}
	form.myButton.value = 'Submitting form...';
	form_being_submitted = true;
	return true; /* submit form */
};

const resetForm = function (form) {
	form.myButton.disabled = false;
	form.myButton.value = 'Submit';
	form_being_submitted = false;
};
