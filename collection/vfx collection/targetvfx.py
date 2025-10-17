entries: map[hash,embed] = {




# VFX_HUB_NAME: signature2
# VFX_HUB_DESCRIPTION: signature2
# VFX_HUB_CATEGORY: target
# VFX_HUB_EMITTERS: 1
    "signature2" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                isSingleParticle: flag = true
                emitterName: string = "Signature"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 0, -200 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                pass: i16 = 500
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 5 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { -100, 130, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0179999992
                        }
                        values: list[vec3] = {
                            { 1, 0, 0.400000006 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Vayne_Skin15_LWX_Signature_signature2.dds"
            }
        }
        particleName: string = "signature2"
        particlePath: string = "signature2"
        transform: mtx44 = {
            1.10000002, 0, 0, 0
            0, 1.10000002, 0, 0
            0, 0, 1.10000002, 0
            -5, 0, 0, 1
        }
    }

     "Characters/Aurora/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "testassetpath3" = "testassetpath3"
            
            "sa" = "sa"
            "targettest" = "targettest"
            "signature2" = "signature2"
        }
     }
} 
