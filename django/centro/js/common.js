/**
 * This function dynamically loads the sizes dropdown, regarding
 * of which size group element has been selected. It is called
 * from the onChange event of the size groups dropdown in the Item
 * edit form.-
 * 
 * @param event				The event DOM object.
 * @param dropdown			The dropdown DOM object that has to be refreshed.-
 * @param request_address	From where to get the list of sizes of a given 
 * 							size group.-
 */
function load_sizes (event, dropdown, request_address)
{
	//
	// This is the currently selected size group
	//
	var size_group_id = event.target.value;
	
	//
	// Check that we received a valid target address
	//
	if (request_address)
	{
		//
		// Set up the target address
		//
		var target_address = request_address + '/' + size_group_id;
		
		//
		// Ask the controller to search the sizes of this size group
		//
		$.get  (target_address,				// Target address to read from 
				'', 						// Data added to the requested address
				function (response)			// A callback function executed on success
				{
				   //
			       // Did we get any code to insert?
			       //
				   if (response.html)
				   {
					   //
					   // Generate a new dropdown with the received code
					   //
					   var jq_dropdown = jQuery (dropdown);
					   
				       jq_dropdown.parent ( ).html (response.html);
				   }
			    },
			    'json');					// The expected server response data type from the server
	}
	
	//
	// Do not allow the anchor to redirect
	//
	return false;	
}



/**
 * Displays a message on the lower part of the current 
 * page (i.e. the feedback bar). If the text parameter
 * is empty, any message that was previously displayed
 * is hidden.-
 * 
 * @param text				The text to be displayed.
 * @param is_error			Whether the text is an error message.
 * @param is_fading			Whether to display a fading animation of the message.
 */
function set_feedback (text, is_error, is_fading)
{
	//
	// The number of milliseconds a message should be displayed
	//
	var message_delay = 1000;
	
	//
	// Do we have anything to show?
	//
	if (text != '')
	{
		//
		// Are we goind to display an error message?
		//
		if (is_error)
		{
			//
			// Change the style to that of an error message
			//
			$('#feedback_bar').removeClass ( ).addClass ('error_message');
			message_delay = 1500;
		}
		else
		{
			//
			// Change the style to that of an informational message
			//
			$('#feedback_bar').removeClass ( ).addClass ('success_message');
			message_delay = 1000;
		}
		
		//
		// Set the corresponding text to be displayed inside the <p> element
		//
		$("#feedback_bar p:first").text (text);
		
		//
		// Activate the message bar
		//
		$('#feedback_bar').css ('display', 'block');
		
		//
		// Leave the message displayed or make it slowly fade?
		//
		if (is_fading)
		{
			//
			// Make the message fade after 'message_delay' ms. 
			// We must show it again, otherwise it will stay
			// invisible for future calls.
			//
			$('#feedback_bar').delay   (message_delay)
							  .fadeOut (message_delay / 10)
							  .delay   (message_delay / 10)
							  .show    ( );
		}
	}
	else
	{
		//
		// Hide the message bar
		//
		$('#feedback_bar').css ('display', 'none');
	}
}


/**
 * This function handles validation and submit of data 
 * in forms across the application. It is usually called 
 * through the onClick event of anchors and buttons.-
 * 
 * @param event		The event DOM object.
 * @param form		The form DOM object that should be validated 
 * 					and submitted (e.g. document.forms[0]).-
 */
function validate_form_data (event, form)
{
	//
	// This is the object that triggered the event
	//
	var source_object = event.target;

	//
	// Create a JQuery object from the form 
	// element received as parameter
	//
	var jq_form = jQuery (form);
	
	//
	// Try to submit the form, displaying 
	// info and error messages accordingly
	//
	jq_form.ajaxSubmit (
		{
			dataType: 'json',
			
			success:function (response)
			{
				//
				// If the success flag is set, there were no errors
			    //
				if (response.success)
				{
					set_feedback (response.message, false, true);
					
					//
					// Did we get any address to go to?
					//
					if (response.follow_address)
					{
						//
						// Wait a little bit and go there
						//
						setTimeout ("window.location = '" + response.follow_address + "'",
								    800);
					}
				}
				else
				{
					set_feedback (response.message, true, true);
				}
			}
		});
	
	//
	// Do not allow the anchor to redirect
	//
	return false;	
}



/**
 * This function handles deleting an element (i.e. record) displayed in 
 * a table (usually) containing all table rows.-
 * This function is usually called through the onClick event of anchors and buttons.-
 * 
 * @param event		The event DOM object.
 */
function delete_table_row (event)
{
	//
	// This is the object that triggered the event
	//
	var source_object = event.target;

	//
	// Check that we received a valid target address
	//
	if (source_object.href)
	{
		//
		// Call the target address and capture its response
		//
		$.get (source_object.href,		// Target address to read from 
			   '',						// Data added to the requested address
			   function (response)		// A callback function executed on success
			   {
				   if (response.success)
				   {
					   //
					   // Display the success message (without fading)
					   //
				       set_feedback (response.message, false, true);
				       
				       //
				       // Wait 1 second before reloading the whole table
				       //
				       setTimeout ("window.location.reload ( )", 1000);
				   }
				   else
				   {
				      set_feedback (response.message, true, true);
				   }
			   },
			   'json');					// The expected data type from the server		
	}

	//
	// Do not allow the anchor to redirect
	//
	return false;	
}
