CREATE TABLE Form( pk_Form BIGINT IDENTITY(1,1) NOT NULL, Name VARCHAR(100) NOT NULL, LabelFR VARCHAR(300) NOT NULL, LabelEN VARCHAR(300) NOT NULL, CreationDate DATETIME NOT NULL, ModificationDate DATETIME NULL, CurStatus TINYINT NOT NULL, DescriptionFR VARCHAR(MAX) NOT NULL, DescriptionEN VARCHAR(MAX) NOT NULL CONSTRAINT pk_Form PRIMARY KEY CLUSTERED (pk_Form) ) CREATE TABLE KeyWord ( pk_KeyWord BIGINT IDENTITY(1,1) NOT NULL, Name VARCHAR(100) NOT NULL UNIQUE, CreationDate DATETIME NOT NULL, ModificationDate DATETIME NULL, CurStatus TINYINT NOT NULL, Lng VARCHAR(2) NOT NULL CHECK (Lng IN('FR', 'EN')) CONSTRAINT pk_KeyWord PRIMARY KEY CLUSTERED (pk_KeyWord ) ) CREATE TABLE KeyWord_Form ( pk_KeyWord_Form BIGINT IDENTITY(1,1) NOT NULL, fk_KeyWord BIGINT NOT NULL, fk_Form BIGINT NOT NULL, CreationDate DATETIME NOT NULL, CurStatus TINYINT NOT NULL, CONSTRAINT pk_KeyWord_Form PRIMARY KEY CLUSTERED (pk_KeyWord_Form), CONSTRAINT KeyWord_Form_fk_KeyWord FOREIGN KEY (fk_KeyWord) REFERENCES KeyWord(pk_KeyWord), CONSTRAINT KeyWord_Form_fk_Form FOREIGN KEY (fk_Form) REFERENCES Form(pk_Form) ) CREATE TABLE Unity ( pk_Unity BIGINT IDENTITY(1,1) NOT NULL, Name VARCHAR(300) NOT NULL, LabelFR VARCHAR(300) NULL, LabelEN VARCHAR(300) NULL, CONSTRAINT pk_Unity PRIMARY KEY CLUSTERED (pk_Unity) ) CREATE TABLE ConfiguratedInput ( pk_ConfiguratedInput BIGINT IDENTITY(1,1) NOT NULL, Name VARCHAR(100) NOT NULL, LabelFR VARCHAR(300) NOT NULL, LabelEN VARCHAR(300) NOT NULL, IsRequired BIT NOT NULL, IsReadOnly BIT NOT NULL, FieldSizeEdit VARCHAR(100) NOT NULL, FieldSizeDisplay VARCHAR(100) NOT NULL, IsEOL BIT NOT NULL, StartDate DATETIME NOT NULL, CurStatus TINYINT NOT NULL, EditorClass VARCHAR(255) NULL, FieldClassEdit VARCHAR(255) NULL, FieldClassDisplay VARCHAR(255) NULL, InputType VARCHAR(255) NOT NULL, CONSTRAINT pk_ConfiguratedInput PRIMARY KEY CLUSTERED (pk_ConfiguratedInput ), ) CREATE TABLE ConfiguratedInputProperty ( pk_ConfiguratedInputProperty BIGINT IDENTITY(1,1) NOT NULL, fk_ConfiguratedInput BIGINT NOT NULL, Name VARCHAR(255) NOT NULL, Value VARCHAR(255) NOT NULL, CreationDate DateTime NOT NULL, ValueType VARCHAR(10) NOT NULL CHECK (ValueType IN('Boolean', 'Number', 'Double', 'String')) CONSTRAINT pk_ConfiguratedInputProperty PRIMARY KEY CLUSTERED (pk_ConfiguratedInputProperty ) CONSTRAINT ConfiguratedInputProperty_fk_Input FOREIGN KEY (fk_ConfiguratedInput) REFERENCES ConfiguratedInput(pk_ConfiguratedInput) ) CREATE TABLE Input ( pk_Input BIGINT IDENTITY(1,1) NOT NULL, fk_form BIGINT NOT NULL, Name VARCHAR(100) NOT NULL, LabelFR VARCHAR(300) NOT NULL, LabelEN VARCHAR(300) NOT NULL, IsRequired BIT NOT NULL, IsReadOnly BIT NOT NULL, FieldSize VARCHAR(100) NOT NULL, IsEOL BIT NOT NULL, StartDate DATETIME NOT NULL, CurStatus TINYINT NOT NULL, EditorClass VARCHAR(255) NULL, FieldClass VARCHAR(255) NULL, InputType VARCHAR(255) NOT NULL, CONSTRAINT pk_Input PRIMARY KEY CLUSTERED (pk_Input ), CONSTRAINT Input_fk_form FOREIGN KEY (fk_form) REFERENCES form(pk_form) ) CREATE TABLE InputProperty ( pk_InputProperty BIGINT IDENTITY(1,1) NOT NULL, fk_Input BIGINT NOT NULL, Name VARCHAR(255) NOT NULL, Value VARCHAR(255) NOT NULL, CreationDate DateTime NOT NULL, ValueType VARCHAR(10) NOT NULL CHECK (ValueType IN('Boolean', 'Number', 'Double', 'String')) CONSTRAINT pk_InputProperty PRIMARY KEY CLUSTERED (pk_InputProperty ) CONSTRAINT InputProperty_fk_Input FOREIGN KEY (fk_Input) REFERENCES Input(pk_Input) )