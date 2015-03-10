<!-- THE RIGHT COLUMN -->
<div id="right_column">

    <!-- ALL SEARCHES START FROM HERE -->
    <div id="search_panel">
        <div id="search_element">
            <?php
                echo '<input onfocus="this.select ( )" type="text"'; 
                echo ' name="search-string"  value="' . $this->lang->line ('common_search') . ' ..."';
                echo '  id="search-string"/>';
                
                //
                // This code is generated inside the controller
                //
                echo $item_search_button; 
            ?>
        </div>
        <div id="customer_element">
            <?php
                //
                // This code is generated inside the controller
                //
                echo $customer_button; 
            ?>
		</div>
    </div>
    
    <!-- THE CURRENTLY SELECTED CUSTOMER -->
    <div id="selected_customer">
        <p><?php echo $customer_name; ?></p>
    </div>
    
    <!-- THE RESULTS OF ALL SEARCHES ARE DISPLAYED HERE THROUGH AJAX -->
    <div id="search_results_panel">
        <div id="amount_payed">
            <div id="amount_payed_text">
		        <?php 
		        //
		        // Display this content only if we have data
		        // about the payment of this sale.-
		        //
		        if (isset ($amount_payed))
		        { 
		            echo '<h3>' . $this->lang->line ('sales_amount_payed') . '</h3>';
		        }
		        ?>
            </div>            
            <div id="amount_payed_value">
                <?php 
                //
                // Display this content only if we have data
                // about the payment of this sale.-
                //
                if (isset ($amount_payed))
                { 
                    echo '<h3>' . $amount_payed . '</h3>';
                }
                ?>            
            </div>
        </div>

        <div id="amount_payed">
            <div id="amount_payed_text">
                <?php 
                //
                // Display this content only if we have data
                // about the payment of this sale.-
                //
                if (isset ($amount_due))
                { 
                    echo '<h3>' . $this->lang->line ('sales_amount_due') . '</h3>';
                }
                ?>
            </div>            
            <div id="amount_payed_value">
                <?php 
                //
                // Display this content only if we have data
                // about the payment of this sale.-
                //
                if (isset ($amount_due))
                { 
                    echo '<h3>' . $amount_due . '</h3>';
                }
                ?>            
            </div>
        </div>

	    <!-- SUBTOTAL AND TAXES -->
	    <div id="subtotal_and_taxes">
		    <div id="subtotal_and_taxes_value">
		        <?php
		        echo '<p>'. $this->lang->line ('sales_subtotal_without_taxes') . '</p>' . $subtotal;
		        ?>
		    </div>
	        <div id="subtotal_and_taxes_value">
	            <?php
	            echo '<p>'. $this->lang->line ('sales_tax') . '</p>' . $taxes;
	            ?>
	        </div>
        </div>
    </div>

    <!-- TOTAL -->
    <div id="total">
    	<?php 
       	echo $total;
        ?>
    </div>
</div>
