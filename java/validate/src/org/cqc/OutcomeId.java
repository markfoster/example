package org.cqc;
// Generated 24-May-2012 12:01:54 by Hibernate Tools 3.2.2.GA



/**
 * OutcomeId generated by hbm2java
 */
public class OutcomeId  implements java.io.Serializable {


     private String providerId;
     private String locationId;
     private String outcomeId;

    public OutcomeId() {
    }

    public OutcomeId(String providerId, String locationId, String outcomeId) {
       this.providerId = providerId;
       this.locationId = locationId;
       this.outcomeId = outcomeId;
    }
   
    public String getProviderId() {
        return this.providerId;
    }
    
    public void setProviderId(String providerId) {
        this.providerId = providerId;
    }
    public String getLocationId() {
        return this.locationId;
    }
    
    public void setLocationId(String locationId) {
        this.locationId = locationId;
    }
    public String getOutcomeId() {
        return this.outcomeId;
    }
    
    public void setOutcomeId(String outcomeId) {
        this.outcomeId = outcomeId;
    }


   public boolean equals(Object other) {
         if ( (this == other ) ) return true;
		 if ( (other == null ) ) return false;
		 if ( !(other instanceof OutcomeId) ) return false;
		 OutcomeId castOther = ( OutcomeId ) other; 
         
		 return ( (this.getProviderId()==castOther.getProviderId()) || ( this.getProviderId()!=null && castOther.getProviderId()!=null && this.getProviderId().equals(castOther.getProviderId()) ) )
 && ( (this.getLocationId()==castOther.getLocationId()) || ( this.getLocationId()!=null && castOther.getLocationId()!=null && this.getLocationId().equals(castOther.getLocationId()) ) )
 && ( (this.getOutcomeId()==castOther.getOutcomeId()) || ( this.getOutcomeId()!=null && castOther.getOutcomeId()!=null && this.getOutcomeId().equals(castOther.getOutcomeId()) ) );
   }
   
   public int hashCode() {
         int result = 17;
         
         result = 37 * result + ( getProviderId() == null ? 0 : this.getProviderId().hashCode() );
         result = 37 * result + ( getLocationId() == null ? 0 : this.getLocationId().hashCode() );
         result = 37 * result + ( getOutcomeId() == null ? 0 : this.getOutcomeId().hashCode() );
         return result;
   }   


}


