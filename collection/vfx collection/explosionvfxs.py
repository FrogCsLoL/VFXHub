entries: map[hash,embed] = {
    #addvfxsystemswithrightbrackets
    
    "insertvfxsystemname4" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            #insertvfxemitterdefinitiondatahere
        }
        particleName: string = "insertvfxsystemname4"
        particlePath: string = "insertvfxsystemname4"
    }
    #dontcreatenewresourceresolver
    "Characters/Aurora/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "insertvfxsystemname" = "insertvfxsystemname"
            
        }
    }
}
