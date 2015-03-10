<?php

/**
 * Tests CRUD functionality of different models.-
 */
class CRUDTest extends CDbTestCase
{
	/**
	 * Compares the content of $object with the row retrieved.-
	 * 
	 * @param Model   $model
	 * @param int     $id
	 * @param  $object
	 */
    private function _testRead ($companyId, $companyObj)
    {
        //
        // Read an existing Company
        //
        $readCompany = Company::model ( )->findByPk ($companyId);

        $this->assertTrue ($readCompany instanceOf Company);
        $this->assertEquals ($readCompany->name,           $companyObj->name);
        $this->assertEquals ($readCompany->address,        $companyObj->address);
        $this->assertEquals ($readCompany->identification, $companyObj->identification);
    }
	
    
	/**
     * Tests the Create, Read, Update and Delete functionality of the model.-
     */
    public function testCRUD ( )
    {
    	//
    	// Create a new Company
    	//
    	$newCompany = new Company ( );
    	
    	$newCompany->setAttributes (array (
    	               'name'           => 'Test Company Name',
    	               'address'        => 'Test Company Address',
    	               'identification' => 'Test Company Identification'));
    	
    	$this->assertTrue ($newCompany->save (false));
    	
    	//
    	// Read an existing Company
    	//
    	$this->_testRead ($newCompany->id, $newCompany);
    	
    	//
    	// Update an existing Company
    	//
    	$updatedName           = 'Updated Company Name';
    	$updatedAddress        = 'Updated Company Address';
    	$updatedIdentification = 'Updated Company Identification';
    	
    	$newCompany->name           = $updatedName;
    	$newCompany->address        = $updatedAddress;
    	$newCompany->identification = $updatedIdentification;
    	
    	$this->assertTrue ($newCompany->save (false));
    	
    	//
    	// Read back the Company again to ensure that the update worked
    	//
    	$this->_testRead ($newCompany->id, $newCompany);
    	
    	//
    	// Delete an existing Company
    	//
    	$newCompanyId = $newCompany->id;
    	$this->assertTrue ($newCompany->delete ( ));
    	
    	$deletedCompany = Company::model ( )->findByPk ($newCompanyId);
    	$this->assertEquals ($deletedCompany, NULL);
    }
	
    
	/**
	 * Check that we may connect to the database with the settings
	 * in config/main.php
	 */
    public function testConnection ( )
    {
    	$this->assertNotEquals (Yii::app ( )->db, NULL);
    }	
}

?>