entries: map[hash,embed] = {

# VFX_HUB_NAME: ebay
# VFX_HUB_DESCRIPTION: ebayname
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 6
    "ebay" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "Flash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/vfxhub/ahri_skin88_color-hold.skins_ahri_skin88_ebay.tex"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.489997715, 1, 0.960006118, 0.579995394 }
                }
                pass: i16 = 5
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 180, 180 }
                }
            }
        }
        particleName: string = "ebay"
        particlePath: string = "ebay"
    }

    "Characters/Aurora/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Aurora_Base_Emote_Dance" = "Aurora_Base_Emote_Dance"
            "ebay" = "ebay"
        }
    }
} 
