entries: map[hash,embed] = {

# VFX_HUB_NAME: testassetpath3
# VFX_HUB_DESCRIPTION: testassetpath3
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 3
    "testauravfx" = VfxSystemDefinitionData {
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
        particleName: string = "testauravfx"
        particlePath: string = "testauravfx"
    }

# VFX_HUB_NAME: cherryblossomauravfx
# VFX_HUB_DESCRIPTION: cherryblossomauravfx
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 1
    "cherryblossomauravfx" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 75
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.699999988
                        }
                    }
                }
                lifetime: option[f32] = {
                    9999
                }
                particleLinger: option[f32] = {
                    2.25
                }
                emitterName: string = "Petals"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 200, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 200, 1 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 3, 2 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 80, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 80, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0.200000003
                            0.5
                        }
                        values: list[f32] = {
                            0
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 100
                    height: f32 = 50
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.278431386, 0.749019623, 0.659998477 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.25
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 0.278431386, 0.749019623, 1 }
                        }
                    }
                }
                alphaRef: u8 = 0
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
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
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 12, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 12, 12, 0 }
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
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jhin_base_Rose_petals_cherryblossomauravfx.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "cherryblossomauravfx"
        particlePath: string = "cherryblossomauravfx"
    }

     "Characters/Aurora/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "testauravfx" = "testauravfx"
            "cherryblossomauravfx" = "cherryblossomauravfx"
        }
     }
} 
