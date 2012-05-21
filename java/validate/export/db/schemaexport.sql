
    drop table if exists etl.provider;

    create table etl.provider (
        provider_id varchar(30) not null,
        provider_name varchar(255),
        in_process varchar(1),
        provider_type varchar(50),
        also_known_as varchar(100),
        address1 varchar(255),
        address2 varchar(255),
        towncity varchar(255),
        county varchar(255),
        postcode varchar(16),
        latitude decimal(10,8),
        longitude decimal(10,8),
        type_info_1 varchar(50),
        type_info_2 varchar(50),
        under_review_text varchar(255),
        telephone varchar(20),
        email varchar(100),
        website varchar(100),
        fax varchar(20),
        is_partnership varchar(1),
        hashvalue varchar(32),
        action char(1),
        primary key (provider_id)
    );
