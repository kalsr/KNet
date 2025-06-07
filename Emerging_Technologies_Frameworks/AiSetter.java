// Artificial Intelligence Setter Class  
//DEPARTMENT OF DEFENSE ARTIFICIAL INTELLIGENCE,STANDARD TAXONOMY - CLASS (SETTER & GETTER METHODS)- Developed On 10-15-2018.

public class AiSetter
{
// DISA Taxonomy Field Declarations



private String ModelingSimulation;
private String DeepLearning;
private String MachineLearning;
private String NaturalLanguageProcessing;
private String DataMining;
private String SuperComputing;
private String NeuroMorphicEngineering;
private String QuantumComputing;
private String VirtualReality;
private String ComputerVision;
private String VirtualAgents;


// Mutator Methods

public void setModelingSimulation(String MSimulation)
{ 
ModelingSimulation = MSimulation;
}
public void setDeepLearning (String DLearning)
{ 
DeepLearning = DLearning;
}
public void setMachineLearning (String MLearning)
{ 
MachineLearning = MLearning;
}
public void setSuperComputing (String SupComputing)
{
 SuperComputing = SupComputing;
}
public void setNaturalLanguageProcessing(String NLProcessing)
{
NaturalLanguageProcessing = NLProcessing;
}
public void setDataMining (String DMining)
{
 DataMining = DMining;
}
public void setNeuroMorphicEngineering(String NMEngineering)
{
NeuroMorphicEngineering = NMEngineering;
}
public void setQuantumComputing (String QComputing)
{ 
QuantumComputing = QComputing;
}
public void setVirtualReality (String VReality)
{
VirtualReality = VReality;
}
public void setComputerVision (String CompVision)
{
ComputerVision = CompVision;
}

public void setVirtualAgents (String VAgents)
{
VirtualAgents = VAgents;
}


// Accessor Methods

public String getModelingSimulation()
{ 
return ModelingSimulation.toUpperCase();
}

public String getDeepLearning()
{ 
return DeepLearning.toUpperCase();
}

public String getMachineLearning ()
{ 
return MachineLearning.toUpperCase();
}

public String getSuperComputing ()
{
 return SuperComputing.toUpperCase();
}

public String getNaturalLanguageProcessing ()
{ 
return NaturalLanguageProcessing.toUpperCase();
}

public String getDataMining ()
{
return DataMining.toUpperCase();
}

public String getNeuroMorphicEngineering ()
{
 return NeuroMorphicEngineering.toUpperCase();
}

public String getQuantumComputing ()
{ 
return QuantumComputing.toUpperCase();
}

public String getVirtualReality ()
{ 
return VirtualReality.toUpperCase();
}

public String getComputerVision ()
{ 
return ComputerVision.toUpperCase();
}

public String getVirtualAgents ()
{ 
return VirtualAgents.toUpperCase();
}


}
