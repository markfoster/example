package org.cqc.etl.model.dao.pptest2.impl;

import com.felees.hbnpojogen.persistence.impl.GenericHibernateDaoImpl;
import org.cqc.etl.model.obj.pptest2.NominatedIndividualPK;
import org.springframework.stereotype.Repository;
import org.cqc.etl.model.dao.pptest2.NominatedIndividualPKDao;
import java.io.Serializable;
 
/**
 * DAO for table: NominatedIndividualPK.
 * @author autogenerated
 */
@Repository
public class NominatedIndividualPKDaoImpl extends GenericHibernateDaoImpl<NominatedIndividualPK, Serializable> implements NominatedIndividualPKDao {
	
	/** Constructor method. */
		public NominatedIndividualPKDaoImpl() {
			super(NominatedIndividualPK.class);
		}
	}

