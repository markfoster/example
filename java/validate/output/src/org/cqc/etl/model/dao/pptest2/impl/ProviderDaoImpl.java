package org.cqc.etl.model.dao.pptest2.impl;

import com.felees.hbnpojogen.persistence.impl.GenericHibernateDaoImpl;
import org.cqc.etl.model.obj.pptest2.Provider;
import org.springframework.stereotype.Repository;
import org.cqc.etl.model.dao.pptest2.ProviderDao;
 
 
/**
 * DAO for table: Provider.
 * @author autogenerated
 */
@Repository
public class ProviderDaoImpl extends GenericHibernateDaoImpl<Provider, String> implements ProviderDao {
	
	/** Constructor method. */
		public ProviderDaoImpl() {
			super(Provider.class);
		}
	}

