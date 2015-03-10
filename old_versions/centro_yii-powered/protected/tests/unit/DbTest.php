<?php

/**
 * Test cases for Database connectivity.-
 */
class DbTest extends CTestCase
{
    /**
     * Check that the database definition file exists and it is readable.-
     */
    public function testExistanceOfDbDefinitionFile ( )
    {
    	$db_schema_path = Yii::app ( )->basePath . '/data/centro.schema.sql';
        $this->assertFileExists ($db_schema_path);
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