package org.cqc.etl.model.obj.pptest2.iface;
import javax.persistence.Basic;


/** 
 * Object interface mapping for hibernate-handled table: partner.
 * @author autogenerated
 */

public interface IPartnerPK {



    /**
     * Return the value associated with the column: partnerId.
	 * @return A String object (this.partnerId)
	 */
	String getPartnerId();
	

  
    /**  
     * Set the value related to the column: partnerId.
	 * @param partnerId the partnerId value you wish to set
	 */
	void setPartnerId(final String partnerId);

    /**
     * Return the value associated with the column: providerId.
	 * @return A String object (this.providerId)
	 */
	String getProviderId();
	

  
    /**  
     * Set the value related to the column: providerId.
	 * @param providerId the providerId value you wish to set
	 */
	void setProviderId(final String providerId);

	// end of interface
}