/**
 * Listener function, if a user was selected.-
 * 
 * @param event		The event DOM object.-
 * @param user_name	The username that should be appended as form data.-
 * @param form  	A form DOM object that will be appended the username.-
 */
function user_selected (event, user_name, form)
{
	//
	// This is the object that triggered the event
	//
	var source_object = event.target;
	
	//
	// Check that this object has an ID
	//
	if (!source_object.id)
	{
		//
		// No ID. This means that the user clicked
		// on the IMG element instead of the A one.
		//
		source_object = source_object.parentNode;
	}

	//
	// Check (again) that this object has an ID
	//
	if (source_object.id)
	{
		//
		// Hide all A elements that didn't trigger the event
		// (i.e. hide all non-selected users)
		//
		var selector = "a:not('#" + source_object.id + "')";
		$(selector).css ("opacity", "0");

		//
		// Hide the welcome message and show the keypad
		//
		$('#welcome_panel').css ('z-index', '-1');
		$('#passwd_panel').css  ('z-index', '1');
		
		//
		// Append the username as a hidden input field
		//
		var js_form = jQuery (form);
		
		js_form.append ('<input type="hidden" name="username" value="' + user_name + '"/>');
	}
		
	//
	// Don't let the browser redirect
	//
	return (false);
}



/**
 * Listener function, if a virtual key was pressed.-
 * 
 * @param event  The event DOM object.-
 * @param target A DOM object where the numbers (or actions) should
 * 				 be applied. It is usually an INPUT element.- 
 */
function keypad_pressed (event, target_element)
{
	//
	// This is the object that triggered the event
	//
	var source_object = event.target;
	
	//
	// This is the element where the action should be applied
	//
	var js_target = jQuery (target_element);
	
	//
	// Check if there is an action to be applied.
	// Else we will just change the content of the target_element.
	//
	switch (source_object.id)
	{
		case 'clear':
			//
			// Clear the content of the target element
			//
			js_target.val ('');
			break;
			
		default:
			//
			// Append the source_object's ID to the content
			//
			js_target.val (jQuery.trim (js_target.val ( )) + source_object.id);
	}
}
