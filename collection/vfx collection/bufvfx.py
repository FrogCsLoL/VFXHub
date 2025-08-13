entries: map[hash,embed] = {

# VFX_HUB_NAME: testbufvfx
# VFX_HUB_DESCRIPTION: testbufvfx
# VFX_HUB_CATEGORY: buf
# VFX_HUB_EMITTERS: 3
    "testbufvfx" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    1.5
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 500, 0 }
                }
                emitterName: string = "Pantheon"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 200, 0, 0 }
                        }
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.741176486, 0, 0.109803922, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0524934381
                            0.183727041
                            0.471128613
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.216049388 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/sett_skin45_energy_trail_testassetpath3.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    0.25
                }
                lifetime: option[f32] = {
                    1.5
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 100, 0 }
                }
                emitterName: string = "Pantheon1"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 700, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0392156877, 0.0392156877, 0.0392156877, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.586614192
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.489997715 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.60104984
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0.19421488, 0.60104984, 0.60104984 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/sett_skin45_fire_trail_graphic_testassetpath3.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    0.25
                }
                lifetime: option[f32] = {
                    1.5
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 100, 0 }
                }
                emitterName: string = "Pantheon2"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 700, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0392156877, 0.0392156877, 0.0392156877, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.586614192
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.0392156877, 0.0392156877, 0.0392156877, 0 }
                            { 0.0392156877, 0.0392156877, 0.0392156877, 1 }
                            { 0.0392156877, 0.0392156877, 0.0392156877, 1 }
                            { 0.0392156877, 0.0392156877, 0.0392156877, 0.90196079 }
                            { 0.0392156877, 0.0392156877, 0.0392156877, 0.772549033 }
                            { 0.0392156877, 0.0392156877, 0.0392156877, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.60104984
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0.19421488, 0.60104984, 0.60104984 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/sett_skin45_fire_trail_graphic_testassetpath3.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
            }
        }
        particleName: string = "testbufvfx"
        particlePath: string = "testbufvfx"
    }

# VFX_HUB_NAME: caitlyncam
# VFX_HUB_DESCRIPTION: caitlyncam
# VFX_HUB_CATEGORY: buf
# VFX_HUB_EMITTERS: 6
    "caitlyncam" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                lifetime: option[f32] = {
                    6
                }
                isSingleParticle: flag = true
                emitterName: string = "BG_Geo"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 115, 0, 100 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/OverlayGeo_caitlyncam.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.200000003
                            0.300000012
                        }
                        values: list[vec4] = {
                            { 0.549019635, 0, 1, 1 }
                            { 0.549019635, 0, 1, 0.500007629 }
                        }
                    }
                }
                pass: i16 = -5
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 5
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.25
                            0.600000024
                            0.875
                            0.949999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 1, 1, 1.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1.25 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Caitlyn_Skin22_OverlayBG_caitlyncam.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                lifetime: option[f32] = {
                    6
                }
                isSingleParticle: flag = true
                emitterName: string = "MotionLines_Geo2"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 115, 0, 100 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/OverlayGeo_caitlyncam.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.78039217, 0.819607854, 0.960784316, 1 }
                }
                pass: i16 = -1
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 5
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.25
                            0.600000024
                            0.875
                            0.949999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 1, 1, 1.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1.25 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Caitlyn_Skin22_MotionLines_caitlyncam.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 5, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 300
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                emitterName: string = "ActionLines"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 0, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    radius: f32 = 250
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0, 1, 0.749996185 }
                }
                pass: i16 = -5
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 30, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 2, 0 }
                            { 1, 3, 0 }
                            { 0, 3, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Caitlyn_Skin22_LongDot_caitlyncam.dds"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                emitterName: string = "InnerActionLines"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 0, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    radius: f32 = 170
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.549019635, 0, 1, 0.300007641 }
                        }
                    }
                }
                pass: i16 = -5
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 30, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 2, 0 }
                            { 1, 3, 0 }
                            { 0, 3, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Caitlyn_Skin22_LongDot_caitlyncam.dds"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                lifetime: option[f32] = {
                    6
                }
                isSingleParticle: flag = true
                emitterName: string = "MotionLines_Geo3"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 115, 0, 100 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/OverlayGeo_caitlyncam.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.78039217, 0.819607854, 0.960784316, 1 }
                }
                pass: i16 = -3
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 5
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.25
                            0.600000024
                            0.875
                            0.949999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 1, 1, 1.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1.25 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Caitlyn_Skin22_MotionLines02_caitlyncam.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 5, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                lifetime: option[f32] = {
                    6
                }
                isSingleParticle: flag = true
                emitterName: string = "Face_Geo1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 115, 0, 100 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/OverlayGeo_caitlyncam.scb"
                    }
                }
                blendMode: u8 = 1
                pass: i16 = -2
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 5
                particleIsLocalOrientation: flag = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.25
                            0.600000024
                            0.875
                            0.949999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 1, 1, 1.5 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1.25 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Caitlyn_Skin22_FaceOnly_caitlyncam.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { -0.899999976, 0 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                        }
                        values: list[vec2] = {
                            { 20, 0 }
                            { 2, 0 }
                            { 0, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0.400000006 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = -10
                }
            }
        }
        particleName: string = "caitlyncam"
        particlePath: string = "caitlyncam"
        soundPersistentDefault: string = "Play_sfx_Caitlyn_CaitlynR_animeoverlay_buffactivate"
        flags: u16 = 197
        mEyeCandy: bool = true
    }





     "Characters/Aurora/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "testbufvfx" = "testbufvfx"
            
            "caitlyncam" = "caitlyncam"
        }
     }
} 
