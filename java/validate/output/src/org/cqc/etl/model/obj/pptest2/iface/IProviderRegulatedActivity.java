package org.cqc.etl.model.obj.pptest2.iface;
import java.util.Date;
import javax.persistence.Basic;
import org.cqc.etl.model.obj.pptest2.ProviderRegulatedActivityPK;


/** 
 * Object interface mapping for hibernate-handled table: provider_regulated_activity.
 * @author autogenerated
 */

public interface IProviderRegulatedActivity {



    /**
     * Return the value associated with the column: actionCode.
	 * @return A String object (this.actionCode)
	 */
	String getActionCode();
	

  
    /**  
     * Set the value related to the column: actionCode.
	 * @param actionCode the actionCode value you wish to set
	 */
	void setActionCode(final String actionCode);

    /**
     * Return the value associated with the column: id.
	 * @return A ProviderRegulatedActivityPK object (this.id)
	 */
	ProviderRegulatedActivityPK getId();
	

  
    /**  
     * Set the value related to the column: id.
	 * @param id the id value you wish to set
	 */
	void setId(final ProviderRegulatedActivityPK id);

    /**
     * Return the value associated with the column: lastUpdated.
	 * @return A Date object (this.lastUpdated)
	 */
	Date getLastUpdated();
	

  
    /**  
     * Set the value related to the column: lastUpdated.
	 * @param lastUpdated the lastUpdated value you wish to set
	 */
	void setLastUpdated(final Date lastUpdated);

	// end of interface
}