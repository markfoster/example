package org.cqc;
// Generated 24-May-2012 12:01:54 by Hibernate Tools 3.2.2.GA


import java.util.Date;

/**
 * ProviderRegulatedActivity generated by hbm2java
 */
public class ProviderRegulatedActivity  implements java.io.Serializable {


     private ProviderRegulatedActivityId id;
     private String actionCode;
     private Date lastUpdated;

    public ProviderRegulatedActivity() {
    }

	
    public ProviderRegulatedActivity(ProviderRegulatedActivityId id) {
        this.id = id;
    }
    public ProviderRegulatedActivity(ProviderRegulatedActivityId id, String actionCode, Date lastUpdated) {
       this.id = id;
       this.actionCode = actionCode;
       this.lastUpdated = lastUpdated;
    }
   
    public ProviderRegulatedActivityId getId() {
        return this.id;
    }
    
    public void setId(ProviderRegulatedActivityId id) {
        this.id = id;
    }
    public String getActionCode() {
        return this.actionCode;
    }
    
    public void setActionCode(String actionCode) {
        this.actionCode = actionCode;
    }
    public Date getLastUpdated() {
        return this.lastUpdated;
    }
    
    public void setLastUpdated(Date lastUpdated) {
        this.lastUpdated = lastUpdated;
    }




}


