entries: map[hash,embed] = {

# VFX_HUB_NAME: test2
# VFX_HUB_DESCRIPTION: test2
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 6
    "Aurora_Base_Emote_Dance" = VfxSystemDefinitionData {
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
                particleColorTexture: string = "ASSETS/vfxhub/test2_texture.tex"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 1 }
                }
                pass: i16 = 5
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
            }
        }
        particleName: string = "Aurora_Base_Emote_Dance"
        particlePath: string = "Aurora_Base_Emote_Dance"
    }

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


# VFX_HUB_NAME: newtest
# VFX_HUB_DESCRIPTION: newtest
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 5
    "newtest" = VfxSystemDefinitionData {
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
                particleColorTexture: string = "ASSETS/vfxhub/newtest_texture.tex"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 1 }
                }
                pass: i16 = 5
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
            }
        }
        particleName: string = "newtest"
        particlePath: string = "newtest"
    }

# VFX_HUB_NAME: blablatest
# VFX_HUB_DESCRIPTION: blablatest
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 10
    "blablatest" = VfxSystemDefinitionData {
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
                particleColorTexture: string = "ASSETS/vfxhub/blablatest_texture.tex"
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 1 }
                }
                pass: i16 = 5
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
            }
        }
        particleName: string = "blablatest"
        particlePath: string = "blablatest"
    }

# VFX_HUB_NAME: testvfx222
# VFX_HUB_DESCRIPTION: testvfx222
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 5
    "testvfx222" =     "Characters/Aurora/Skins/Skin0/Particles/Aurora_Base_R_TravelEnd" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1.5
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "Smoke"
                importance: u8 = 4
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, -10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 10, -10 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    radius: f32 = 5
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 80, -30 }
                }
                falloffTexture: string = "assets/blablablaaurora/defaultfalloff.aurora.tex"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.992156863, 0.996078432, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.992156863, 0.996078432, 1, 1 }
                            { 0.992156863, 0.996078432, 1, 1 }
                            { 0.992156863, 0.996078432, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.603921592, 0.796078444, 1, 0 }
                            { 0.498039216, 0.741176486, 1, 1 }
                            { 0.254901975, 0.615686297, 1, 0.211764708 }
                            { 0.129411772, 0.447058827, 0.788235307, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "assets/blablablaaurora/aurora_base_smokeerode.aurora.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec4] = {
                                { 1, 0, 0, 0 }
                            }
                        }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                depthBiasFactors: vec2 = { -1, -3 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    360
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    360
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.499900013
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.499900013
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                    -0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.499900013
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 13, 60, 60 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 13, 60, 60 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                            { 5, 5, 5 }
                            { 6, 6, 6 }
                        }
                    }
                }
                texture: string = "assets/blablablaaurora/sion_base_sl_dust_01.aurora.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1.5
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "Smoke1"
                importance: u8 = 4
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, -10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 10, -10 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    radius: f32 = 5
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 80, -30 }
                }
                falloffTexture: string = "assets/blablablaaurora/defaultfalloff.aurora.tex"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.533333361, 0.650980413, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.533333361, 0.760784328, 1, 1 }
                            { 0.533333361, 0.760784328, 1, 1 }
                            { 0.533333361, 0.760784328, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.937254906, 0.968627453, 1, 0 }
                            { 0.698039234, 0.843137264, 1, 1 }
                            { 0.0117647061, 0.490196079, 1, 0.209994659 }
                            { 0, 0.482352942, 1, 0 }
                        }
                    }
                }
                pass: i16 = -1
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "assets/blablablaaurora/aurora_base_smokeerode.aurora.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec4] = {
                                { 1, 0, 0, 0 }
                            }
                        }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                depthBiasFactors: vec2 = { -1, -3 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    360
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    360
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.499900013
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.499900013
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                    -0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.499900013
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 13, 60, 60 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 13, 60, 60 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                            { 5, 5, 5 }
                            { 6, 6, 6 }
                        }
                    }
                }
                texture: string = "assets/blablablaaurora/sion_base_sl_dust_01.aurora.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "Flash_Rainbow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 80, -30 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.227450982, 0.600000024, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 170, 170, 170 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 0.300000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "assets/blablablaaurora/common_bigradialhalo.aurora.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 60
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.5
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.25
                }
                emitterName: string = "little_sparks"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 2, 0.200000003 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 500, 200, 0 }
                            { 500, 200, 0 }
                            { 6000, 200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 5, 12 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 50
                    height: f32 = 20
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 80, -30 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.200000003
                            0.400000006
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.666666687, 0.827450991, 1, 1 }
                            { 0.603921592, 0.796078444, 1, 1 }
                            { 0.13333334, 0.552941203, 1, 1 }
                            { 0, 0.482352942, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 0.5, 5, 0 }
                            { 1, 1, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "assets/blablablaaurora/aurora_base_q_glowspecks.aurora.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "onKill_supportingFlash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, -30 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.666666687, 0.827450991, 1, 0.600000024 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.486274511, 0.733333349, 1, 1 }
                            { 0.200000003, 0.552941203, 0.929411769, 0 }
                        }
                    }
                }
                pass: i16 = 10
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.265217394
                            0.469565213
                            0.726086974
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0.367132872, 0, 0 }
                            { 0.199300706, 0, 0 }
                            { 0.083916083, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "assets/blablablaaurora/aurora_base_mis_sparkles.aurora.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 1, 1, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 6, 0, 0 }
                    }
                    paletteCount: i32 = 32
                }
            }
        }
        particleName: string = "testvfx222"
        particlePath: string = "testvfx222"
        flags: u16 = 198
    }

# VFX_HUB_NAME: testvfx333
# VFX_HUB_DESCRIPTION: testvfx333
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 4
    "testvfx333" =     "Characters/Aurora/Skins/Skin0/Particles/Aurora_Base_Emote_JokeRune" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "PortalRing_Red"
                Linger: pointer = VfxLingerDefinitionData {}
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                        }
                        values: list[f32] = {
                            0
                            0
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -75 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "assets/blablablaaurora/aurora_base_q_halfsphere_01.aurora.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.700007617 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.239215687, 0.741176486, 0.909803927, 0 }
                            { 0.294117659, 0.823529422, 1, 1 }
                            { 0.152941182, 0.607843161, 0.760784328, 0 }
                        }
                    }
                }
                pass: i16 = 90
                meshRenderFlags: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                0
                                0
                            }
                        }
                    }
                    erosionMapName: string = "assets/blablablaaurora/aurora_gradmap3.aurora.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.949999988, 0.100000001, 0.949999988 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.00499999989
                            0.0199999996
                            0.0299999993
                            0.699999988
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1.10000002, 1.10000002, 1.10000002 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "assets/blablablaaurora/aurora_passivering01.aurora.tex"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 45
                }
                particleUVRotateRate: embed = IntegratedValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "PortalRing_Blue"
                Linger: pointer = VfxLingerDefinitionData {}
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                        }
                        values: list[f32] = {
                            0
                            0
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -75 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "assets/blablablaaurora/aurora_base_q_halfsphere_01.aurora.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.501960814, 0.698039234, 0.760784328, 0 }
                            { 0.498039216, 0.874509811, 1, 1 }
                            { 0.305882365, 0.654901981, 0.772549033, 0 }
                        }
                    }
                }
                pass: i16 = 91
                meshRenderFlags: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                0
                                0
                            }
                        }
                    }
                    erosionMapName: string = "assets/blablablaaurora/aurora_gradmap3.aurora.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.100000001, 0.899999976 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.00499999989
                            0.0199999996
                            0.0299999993
                            0.699999988
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1.10000002, 1.10000002, 1.10000002 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "assets/blablablaaurora/aurora_passivering01.aurora.tex"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 45
                }
                particleUVRotateRate: embed = IntegratedValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "PortalRing_Add"
                Linger: pointer = VfxLingerDefinitionData {}
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                        }
                        values: list[f32] = {
                            0
                            0
                        }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -75 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "assets/blablablaaurora/aurora_base_q_halfsphere_01.aurora.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.509803951, 0.87843138, 1, 0.5 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 92
                meshRenderFlags: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                0
                                0
                            }
                        }
                    }
                    erosionMapName: string = "assets/blablablaaurora/aurora_gradmap3.aurora.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.100000001, 0.899999976 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.00499999989
                            0.0199999996
                            0.0299999993
                            0.699999988
                            0.800000012
                            0.949999988
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1.10000002, 1.10000002, 1.10000002 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.5, 1.5, 1.5 }
                            { 0.200000003, 0.200000003, 0.200000003 }
                        }
                    }
                }
                texture: string = "assets/blablablaaurora/aurora_passivering01.aurora.tex"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 45
                }
                particleUVRotateRate: embed = IntegratedValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0199999996
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.899999976
                                    1.10000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.800000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 8
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 100
                                dynamics: pointer = VfxAnimatedFloatVariableData {
                                    times: list[f32] = {
                                        0
                                        1
                                    }
                                    values: list[f32] = {
                                        0
                                        100
                                    }
                                }
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "spark_shoot_up5"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 250, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 80, 1, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 80, 1, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {



     "Characters/Aurora/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Aurora_Base_Emote_Dance" = "Aurora_Base_Emote_Dance"
            "ebay" = "ebay"
            "newtest" = "newtest"
            "blablatest" = "blablatest"
            "testvfx222" = "testvfx222"
            "testvfx333" = "testvfx333"
        }
     }
} 
