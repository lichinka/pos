<?php

/**
 * This is the model class for table "yii_company".
 *
 * The following are the available columns in table 'yii_company':
 * 
 * @property integer $id
 * @property string  $name
 * @property string  $address
 * @property string  $identification
 */
class Company extends CActiveRecord
{
	/**
	 * Returns the static model of the specified AR class.
	 * 
	 * @return Company the static model class
	 */
	public static function model ($className = __CLASS__)
	{
		return parent::model ($className);
	}

	/**
	 * @return string the associated database table name
	 */
	public function tableName ( )
	{
		return 'company';
	}

	/**
	 * @return array validation rules for model attributes.
	 */
	public function rules ( )
	{
		// NOTE: you should only define rules for those attributes that
		// will receive user inputs.
		return array (
			array ('name, address, identification', 'required'),
			array ('name, address, identification', 'length', 'max'=>255),
			// The following rule is used by search().
			// Please remove those attributes that should not be searched.
			array ('id, name, address, identification', 'safe', 'on'=>'search'),
		);
	}

	
	/**
	 * @return array relational rules.
	 */
	public function relations ( )
	{
		// NOTE: you may need to adjust the relation name and the related
		// class name for the relations automatically generated below.
		return array ( );
	}

	
	/**
	 * @return array customized attribute labels (name=>label)
	 */
	public function attributeLabels ( )
	{
		return array ('id'             => 'Company',
		              'name'           => 'Name',
		              'address'        => 'Address',
			          'identification' => 'Identification');
	}

	
	/**
	 * Retrieves a list of models based on the current search/filter conditions.
	 * @return CActiveDataProvider the data provider that can return the models based on the search/filter conditions.
	 */
	public function search ( )
	{
		// Warning: Please modify the following code to remove attributes that
		// should not be searched.

		$criteria = new CDbCriteria;

		$criteria->compare ('id',             $this->id);
		$criteria->compare ('name',           $this->name,           true);
		$criteria->compare ('address',        $this->address,        true);
		$criteria->compare ('identification', $this->identification, true);

		return new CActiveDataProvider (get_class ($this), 
		                                array ('criteria'=>$criteria));
	}
}