package org.cqc.etl.model.dao.pptest2.impl;

import com.felees.hbnpojogen.persistence.impl.GenericHibernateDaoImpl;
import org.cqc.etl.model.obj.pptest2.ChapterPK;
import org.springframework.stereotype.Repository;
import org.cqc.etl.model.dao.pptest2.ChapterPKDao;
import java.io.Serializable;
 
/**
 * DAO for table: ChapterPK.
 * @author autogenerated
 */
@Repository
public class ChapterPKDaoImpl extends GenericHibernateDaoImpl<ChapterPK, Serializable> implements ChapterPKDao {
	
	/** Constructor method. */
		public ChapterPKDaoImpl() {
			super(ChapterPK.class);
		}
	}

