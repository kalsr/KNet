// CLOUD SERVICE MODULES - SETTER & Getter Class  
//DEPARTMENT OF DEFENSE CLOUD STANDARD TAXONOMY - CLASS (SETTER & GETTER METHODS)- Developed On 10-17-2018 - (Randy Singh).

public class CloudSetter
{

// CLOUD Taxonomy Field Declarations



private String IaaS;
private String PaaS;
private String SaaS;


// Mutator Methods (Setter)

public void setIaaS(String iaas)
{ 
IaaS = iaas;
}

public void setPaaS(String paas)
{ 
PaaS = paas;
}

public void setSaaS(String saas)
{ 
SaaS = saas;
}



// Accessor Methods (Getter)

public String getIaaS()
{ 
return IaaS.toUpperCase();
}

public String getPaaS()
{ 
return PaaS.toUpperCase();
}

public String getSaaS()
{ 
return SaaS.toUpperCase();
}


} //end-class
