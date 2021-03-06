package org.cqc.etl.model.dao.pptest2.impl;

import com.felees.hbnpojogen.persistence.impl.GenericHibernateDaoImpl;
import org.cqc.etl.model.obj.pptest2.Outcome;
import org.springframework.stereotype.Repository;
import org.cqc.etl.model.dao.pptest2.OutcomeDao;
import org.cqc.etl.model.obj.pptest2.OutcomePK;
 
/**
 * DAO for table: Outcome.
 * @author autogenerated
 */
@Repository
public class OutcomeDaoImpl extends GenericHibernateDaoImpl<Outcome, OutcomePK> implements OutcomeDao {
	
	/** Constructor method. */
		public OutcomeDaoImpl() {
			super(Outcome.class);
		}
	}

