entries: map[hash,embed] = {

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

# VFX_HUB_NAME: fireidle
# VFX_HUB_DESCRIPTION: fireidle
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 4
    "fireidle" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 9
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            9
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "frost_smoke"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1.5, 0 }
                            { 0, 0, 0 }
                            { 0, 1.5, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 9, 5, 9 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.37855997973121824, 0.34584083542630534, 0.4954140665344789, 0.701960802 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.23986270292836875, 0.21752403035343748, 0.3196436764102665, 0.501960814 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 22
                depthBiasFactors: vec2 = { 0, -80 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0, 1 }
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
                            { 0, -0, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.649999976
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 10, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0890493393
                            0.25
                            0.527677476
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0, 0 }
                            { 0.899999976, 0, 0 }
                            { 1, 0, 0 }
                            { 0.75, 0, 0 }
                            { 0.649999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Veigar_Z_Frost_Smoke_Mult.SKINS_Veigar_Skin60_fireidle.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.200000003
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.200000003
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, 2 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Veigar_Z_Frost_Smoke_Mult.SKINS_Veigar_Skin60_fireidle.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, 0.200000003 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        2
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.100000001, 0.200000003 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                emitterName: string = "Fire_"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 30 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            -60
                                            60
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.850003839 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.37855997973121824, 0.34584083542630534, 0.4954140665344789, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.37855997973121824, 0.34584083542630534, 0.4954140665344789, 0 }
                            { 0.3111658427912264, 0.2835326810375897, 0.4098557061970718, 1 }
                            { 0.21931443678230444, 0.1986129558763285, 0.2932482971607901, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 23
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            { 20, 20, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.25, 0 }
                            { 0.5, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Veigar_Z_Buf_NoiseMap_1.SKINS_Veigar_Skin60_fireidle.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, 1 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
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
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                            { 0.5, -0.5 }
                            { -0.5, 0.5 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Veigar_Skin60_Z_Spectral_Mult.SKINS_Veigar_Skin60_fireidle.tex"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 1 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.300000012 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 0.5 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                emitterName: string = "Fire_1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 10 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            -60
                                            60
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.34612282154659607, 0.31602227098479835, 0.453624787838731, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 22
                colorLookUpTypeY: u8 = 3
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            { 20, 20, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.25, 0 }
                            { 0.5, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Veigar_Z_Buf_NoiseMap_1.SKINS_Veigar_Skin60_fireidle.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, 1 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
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
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                            { 0.5, -0.5 }
                            { -0.5, 0.5 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Veigar_Skin60_Z_Spectral_Mult.SKINS_Veigar_Skin60_fireidle.tex"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 1 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 0.5 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                emitterName: string = "frost_smoke1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                drag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1.5, 0 }
                            { 0, 0, 0 }
                            { 0, 1.5, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 9, 5, 9 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.37855997973121824, 0.34584083542630534, 0.4954140665344789, 0.549019635 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.510002315 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 21
                depthBiasFactors: vec2 = { 0, 50 }
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
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
                                    90
                                    180
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.649999976
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 70, 70, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0890493393
                            0.25
                            0.527677476
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0 }
                            { 0.899999976, 0.899999976, 0 }
                            { 1, 1, 0 }
                            { 0.75, 0.5, 0 }
                            { 0.649999976, 0.400000006, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Veigar_Z_Frost_Smoke_Mult.SKINS_Veigar_Skin60_fireidle.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.200000003
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.200000003
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.0500000007, 2 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/light01.SKINS_Veigar_Skin60_fireidle.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, 0.200000003 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        2
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.100000001, 0.200000003 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "fireidle"
        particlePath: string = "fireidle"
    }

# VFX_HUB_NAME: Electricity
# VFX_HUB_DESCRIPTION: Electricity
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 3
    "Electricity" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
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
                                    0.200000003
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    9999
                }
                emitterName: string = "Activate_Electricity"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 15, 0 }
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
                                { 0, 15, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.49000001
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.10000002
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Base_W_tar_flipbook_Electricity.dds"
                frameRate: f32 = 30
                numFrames: u16 = 9
                startFrame: u16 = 1
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
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
                                    0.200000003
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    9999
                }
                emitterName: string = "Activate_Electricity"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 15, 0 }
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
                                { 0, 15, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.49000001
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.10000002
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Base_W_tar_flipbook_Electricity.dds"
                frameRate: f32 = 30
                numFrames: u16 = 9
                startFrame: u16 = 1
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
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
                                    0.200000003
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    9999
                }
                emitterName: string = "Activate_Electricity2"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 15, 0 }
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
                                { 0, 15, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.49000001
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.10000002
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Base_W_tar_flipbook_Electricity.dds"
                frameRate: f32 = 30
                numFrames: u16 = 9
                startFrame: u16 = 1
                texDiv: vec2 = { 3, 3 }
            }
        }
        particleName: string = "Electricity"
        particlePath: string = "Electricity"
    }

# VFX_HUB_NAME: Storm Aura
# VFX_HUB_DESCRIPTION: Storm Aura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 9
    "Storm Aura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            10
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    9999
                }
                particleLinger: option[f32] = {
                    9999
                }
                emitterName: string = "LIghtningJayce"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3000, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 3000, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 40, 15 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    birthTranslation: embed = ValueVector3 {}
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 45, 80, 0 }
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
                                { 45, 80, 0 }
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
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            0.300000012
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 0 }
                            { 0, 0, 0, 1 }
                            { 0.0549019612, 0, 0.839215696, 1 }
                            { 0, 0, 0, 0 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                pass: i16 = 106
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                0.200000003
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Ezreal_Skin21_Q_ErosionShapes01_Storm_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -20 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
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
                            { 90, 10, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 1, 1, 1 }
                            { 1.10000002, 1.10000002, 1.10000002 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Ezreal_Skin21_Q_Lightning02_Storm_Aura.dds"
                numFrames: u16 = 9
                texDiv: vec2 = { 3, 3 }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 35, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
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
                                    0.600000024
                                    1.20000005
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
                lifetime: option[f32] = {
                    9999
                }
                emitterName: string = "Distort_FAST"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 40, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/vfxhub/Storm Aura_texture.tex"
                blendMode: u8 = 1
                pass: i16 = 2
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.00499999989
                    normalMapTexture: string = "ASSETS/vfxhub/distort-pinch_Storm_Aura.dds"
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 175, 175, 175 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Aura_Self_Storm_Aura.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0399999991
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    9999
                }
                isSingleParticle: flag = true
                emitterName: string = "OutsideRing"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0549019612, 0, 0.839215696, 1 }
                            { 0.0549019612, 0, 0.839215696, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
                colorLookUpScales: vec2 = { 1, 0.400000006 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 45, 0 }
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
                                    8
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 45, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 130, 370, 370 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.097508125
                            0.149512455
                            0.236186355
                            0.331527621
                            0.459371626
                            0.645720482
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 0.300000012 }
                            { 0.45991379, 0.462707043, 0.462707043 }
                            { 0.671120703, 0.663196743, 0.663196743 }
                            { 0.812931061, 0.806188941, 0.806188941 }
                            { 0.885344803, 0.882864058, 0.876829624 }
                            { 0.936637938, 0.936023355, 0.936023355 }
                            { 0.978879333, 0.969690859, 0.969690859 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Ezreal_Skin21_P_ShockRing_Storm_Aura.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.0399999991
                }
                particleLinger: option[f32] = {
                    0.0399999991
                }
                lifetime: option[f32] = {
                    9999
                }
                emitterName: string = "STAR2_BURST"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    birthTranslation: embed = ValueVector3 {}
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 35, 200, 0 }
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
                                { 35, 200, 0 }
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
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                pass: i16 = 3
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 230, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.349999994
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 230, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Ezreal_Skin21_E_Star_1_Storm_Aura.dds"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    9999
                }
                isSingleParticle: flag = true
                emitterName: string = "Distort1"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/vfxhub/Storm Aura_texture.tex"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaRef: u8 = 0
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.0199999996
                    normalMapTexture: string = "ASSETS/vfxhub/Ezreal_Skin21_P_Circle_normal_Storm_Aura.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 140, 450, 450 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.300000012, 0.300000012 }
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 0.980000019, 0.980000019, 0.980000019 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Ezreal_Skin21_P_White_Storm_Aura.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.180000007
                }
                lifetime: option[f32] = {
                    9999
                }
                isSingleParticle: flag = true
                emitterName: string = "DistortFAST"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/vfxhub/Storm Aura_texture.tex"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.0120000001
                    distortionMode: u8 = 2
                    normalMapTexture: string = "ASSETS/vfxhub/Ezreal_Skin21_P_Circle_normal_Storm_Aura.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 600, 600 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 0.800000012, 0.699999988, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Ezreal_Skin21_P_White_Storm_Aura.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
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
                                    0.5
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
                    0.649999976
                }
                lifetime: option[f32] = {
                    9999
                }
                emitterName: string = "Clumps"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
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
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0.5, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 120, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 120, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 5, 1 }
                }
                velocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    birthTranslation: embed = ValueVector3 {}
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 110, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.649999976
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
                                { 110, 0, 0 }
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
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[f32] = {
                            0
                            0
                            0
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.0549019612, 0, 0.839215696, 1 }
                            { 0.0549019612, 0, 0.839215696, 0 }
                        }
                    }
                }
                pass: i16 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 22, 22, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 22, 22, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Ezreal_Skin21_P_Dirt_Storm_Aura.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, -1 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.449999988
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    9999
                }
                emitterName: string = "Swirls_Small"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -20, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Ezreal_Skin21_E_AnimeBurstMesh02_Storm_Aura.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.62999922, 0.590005338, 0.579995394, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0.300007641 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.0549019612, 0, 0.839215696, 0 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.0500000007
                    erosionFeatherOut: f32 = 0.0500000007
                    erosionSliceWidth: f32 = 0.349999994
                    erosionMapName: string = "ASSETS/vfxhub/Ezreal_Skin21_E_ErosionSphere02_Storm_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 0.800000012, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0, 6.4000001, 0 }
                            { 0, 5.5999999, 0 }
                            { 0, 1.60000002, 0 }
                            { 0, 0.800000012, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.800000012, 1.5, 0.800000012 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.10000002
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.10000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.800000012, 1.5, 0.800000012 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.18883495
                            0.527139127
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.850087821, 0.75, 0.850087821 }
                            { 1.20000005, 1, 1.20000005 }
                            { 1.60000002, 1.14999998, 1.60000002 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/color-hold_Storm_Aura.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.800000012, 0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.10000002
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.800000012, 0.5 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.60000002
                }
                lifetime: option[f32] = {
                    9999
                }
                emitterName: string = "Swirls_Large"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -20, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Ezreal_Skin21_E_AnimeBurstMesh02_Storm_Aura.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.62999922, 0.590005338, 0.579995394, 0.100007631 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.0549019612, 0, 0.839215696, 0.100007631 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 1, 1, 1, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.0500000007
                    erosionFeatherOut: f32 = 0.0500000007
                    erosionSliceWidth: f32 = 0.349999994
                    erosionMapName: string = "ASSETS/vfxhub/Ezreal_Skin21_E_ErosionSphere02_Storm_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0, 4, 0 }
                            { 0, 3.5, 0 }
                            { 0, 1, 0 }
                            { 0, 0.5, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2.5, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.10000002
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.10000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 2.5, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.18883495
                            0.527139127
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.850087821, 0.75, 0.850087821 }
                            { 1.5, 1, 1.5 }
                            { 2, 1.14999998, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/color-hold_Storm_Aura.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, -1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.10000002
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, -1 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
        }
        particleName: string = "Storm Aura"
        particlePath: string = "Storm Aura"
        soundOnCreateDefault: string = "Play_sfx_EzrealSkin21_EzrealP_cast"
        soundPersistentDefault: string = "Play_sfx_EzrealSkin21_EzrealP_buffactivate"
        flags: u16 = 212
    }

# VFX_HUB_NAME: Hand Flames Aura
# VFX_HUB_DESCRIPTION: Hand Flames Aura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 8
    "Hand Flames Aura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0.100000001 }
                }
                emitterName: string = "AB_Trail1"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 250
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 250, 0, 0 }
                        }
                        mMaxAddedPerFrame: i32 = 500
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.43921569, 0.0431372561, 0, 0.839993894 }
                            { 0.43921569, 0.0431372561, 0, 0.701960802 }
                            { 0.43921569, 0.0431372561, 0, 0.501960814 }
                            { 0.43921569, 0.0431372561, 0, 0 }
                        }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            1
                        }
                        values: list[vec3] = {
                            { 0.25, 0, 0 }
                            { 1, 0, 0 }
                            { 0.25, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Brand_Skin08_Trail_Hand_Flames_Aura.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 150
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                emitterName: string = "A_Trail1"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 250
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 500, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                        mMaxAddedPerFrame: i32 = 500
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.43921569, 0.0431372561, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.43921569, 0.0431372561, 0, 1 }
                            { 0.43921569, 0.0431372561, 0, 0 }
                        }
                    }
                }
                pass: i16 = 50
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 40, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5, 0, 0 }
                            { 1, 0, 0 }
                            { 0.25, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Brand_Skin08_Trail_Hand_Flames_Aura.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -2.79999995, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
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
                                    0.150000006
                                    0.300000012
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    12
                }
                emitterName: string = "Flame_add1"
                importance: u8 = 2
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1000, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1000, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.43921569, 0.0431372561, 0, 1 }
                            { 0.43921569, 0.0431372561, 0, 1 }
                            { 0.43921569, 0.0431372561, 0, 1 }
                            { 0.43921569, 0.0431372561, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.100000001
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -0.300000012
                                    -0.300000012
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
                    constantValue: vec3 = { 2, 2, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                    4
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 2, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 1.5, 1.5, 1 }
                            { 3.25, 3.25, 1 }
                            { 3.29999995, 3.29999995, 1 }
                            { 3.31999993, 3.31999993, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Brand_Skin08_I_Fire_Cas1_Hand_Flames_Aura.dds"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "GlowBall2"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.43921569, 0.0431372561, 0, 0.749019623 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.43921569, 0.0431372561, 0, 0 }
                            { 0.43921569, 0.0431372561, 0, 1 }
                            { 0.43921569, 0.0431372561, 0, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 1.5, 0, 0 }
                            { 1, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Brand_Skin08_Glow3_Hand_Flames_Aura.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "GlowBall3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.43921569, 0.0431372561, 0, 1 }
                }
                pass: i16 = 10
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 10, 0 }
                }
                texture: string = "ASSETS/vfxhub/Brand_Skin08_Glow3_Hand_Flames_Aura.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
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
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                emitterName: string = "HandGlows1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.913725495, 0.913725495, 0.913725495, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.43921569, 0.0431372561, 0, 0 }
                            { 0.43921569, 0.0431372561, 0, 1 }
                            { 0.43921569, 0.0431372561, 0, 1 }
                            { 0.43921569, 0.0431372561, 0, 0 }
                        }
                    }
                }
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
                    constantValue: vec3 = { 60, 20, -1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.100000001, 2.5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Brand_Skin08_I_Sparks_01_Hand_Flames_Aura.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.3000002
                }
                emitterName: string = "flame_blend1"
                importance: u8 = 2
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1000, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1000, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.43921569, 0.0431372561, 0, 0 }
                            { 0.43921569, 0.0431372561, 0, 1 }
                            { 0.43921569, 0.0431372561, 0, 0.741176486 }
                            { 0.43921569, 0.0431372561, 0, 0 }
                        }
                    }
                }
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.100000001
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -0.300000012
                                    -0.300000012
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
                    constantValue: vec3 = { 6.80000019, 9, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 6.80000019, 9, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 2, 2, 1 }
                            { 3, 3, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Brand_Skin08_I_Fire_Cas1_Hand_Flames_Aura.dds"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
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
                    0.5
                }
                emitterName: string = "sparks1"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 1 }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.219999999
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.43921569, 0.0431372561, 0, 0.819607854 }
                            { 0.43921569, 0.0431372561, 0, 1 }
                            { 0.43921569, 0.0431372561, 0, 1 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { -60, 0, 0 }
                            { 60, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 5, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Brand_Skin08_Sparkle_Hand_Flames_Aura.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Hand Flames Aura"
        particlePath: string = "Hand Flames Aura"
    }

# VFX_HUB_NAME: Edgy Aura
# VFX_HUB_DESCRIPTION: Edgy Aura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 8
    "Edgy Aura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 60
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    4
                }
                lifetime: option[f32] = {
                    3000
                }
                emitterName: string = "ShadowWisps"
                birthOrbitalVelocity: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 205, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 205, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 35
                    height: f32 = 100
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/vfxhub/Edgy Aura_texture.tex"
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.90196079 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.933333337, 1, 0, 0.90196079 }
                            { 0.933333337, 1, 0, 0.90196079 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 37.5, 37.5, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.511099994
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1.5
                                    -1
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
                            { 37.5, 37.5, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                            { 0.200000003, 5, 1 }
                            { 1, 3, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/zed_shadowwisps_Edgy_Aura.dds"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
                translationOverride: vec3 = { 0, -250, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.580392182, 0.0392156877, 0.176470593, 0.140001521 }
                }
                pass: i16 = -1
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 350, 350 }
                }
                texture: string = "ASSETS/vfxhub/Akali_Skin14_BackDrop_Edgy_Aura.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3000
                }
                particleLinger: option[f32] = {
                    5
                }
                lifetime: option[f32] = {
                    3000
                }
                isSingleParticle: flag = true
                emitterName: string = "flamering"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0777751058
                            0.191451207
                            0.250181049
                            0.453055173
                            0.77700001
                            1
                        }
                        values: list[vec4] = {
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                        }
                    }
                }
                pass: i16 = 1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/vfxhub/TestVFX_E_Inkpact_01_Erode_Edgy_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 360, 1 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 360, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -2, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, -2, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 130, 300, 300 }
                }
                texture: string = "ASSETS/vfxhub/Akali_Skin14_BackDrop_Edgy_Aura.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { -1, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3000
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    3000
                }
                isSingleParticle: flag = true
                emitterName: string = "flamering1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                }
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.65882355, 0.180392161, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0777751058
                            0.191451207
                            0.250181049
                            0.453055173
                            0.77700001
                            1
                        }
                        values: list[vec4] = {
                            { 0.580392182, 0.0392156877, 0.176470593, 1 }
                            { 0.580392182, 0.0392156877, 0.176470593, 1 }
                            { 0.580392182, 0.0392156877, 0.176470593, 1 }
                            { 0.580392182, 0.0392156877, 0.176470593, 1 }
                            { 0.580392182, 0.0392156877, 0.176470593, 1 }
                            { 0.580392182, 0.0392156877, 0.176470593, 1 }
                            { 0.580392182, 0.0392156877, 0.176470593, 1 }
                        }
                    }
                }
                pass: i16 = 2
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                1.10000002
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/vfxhub/TestVFX_E_Inkpact_01_Erode_Edgy_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 360, 1 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 360, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -2, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, -2, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 140, 250, 250 }
                }
                texture: string = "ASSETS/vfxhub/Akali_Skin14_BackDrop_Edgy_Aura.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { -1, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3000
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    3000
                }
                isSingleParticle: flag = true
                emitterName: string = "flamering2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.486274511, 0.286274523, 0.650980413, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0777751058
                            0.191451207
                            0.250181049
                            0.453055173
                            0.77700001
                            1
                        }
                        values: list[vec4] = {
                            { 0.447058827, 0.0313725509, 0.137254909, 1 }
                            { 0.447058827, 0.0313725509, 0.137254909, 1 }
                            { 0.447058827, 0.0313725509, 0.137254909, 1 }
                            { 0.447058827, 0.0313725509, 0.137254909, 1 }
                            { 0.447058827, 0.0313725509, 0.137254909, 1 }
                            { 0.447058827, 0.0313725509, 0.137254909, 1 }
                            { 0.447058827, 0.0313725509, 0.137254909, 1 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/vfxhub/TestVFX_E_Inkpact_01_Erode_Edgy_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 360, 1 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 360, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -2, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, -2, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 250, 250 }
                }
                texture: string = "ASSETS/vfxhub/Akali_Skin14_BackDrop_Edgy_Aura.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { -1, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3000
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    3000
                }
                isSingleParticle: flag = true
                emitterName: string = "flamering3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0777751058
                            0.191451207
                            0.250181049
                            0.453055173
                            0.77700001
                            1
                        }
                        values: list[vec4] = {
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                            { 0.0800030529, 0.0899977088, 0.130006865, 0.600000024 }
                        }
                    }
                }
                pass: i16 = -3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                1.20000005
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/vfxhub/TestVFX_E_Inkpact_Erode_03_Edgy_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 360, 1 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -90, 360, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -2, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, -2, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 300, 300 }
                }
                texture: string = "ASSETS/vfxhub/Akali_Skin14_BackDrop_Edgy_Aura.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { -1, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3000
                }
                lifetime: option[f32] = {
                    3000
                }
                isSingleParticle: flag = true
                emitterName: string = "up_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -15, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Yone_Skin35_Cylinder_02_Edgy_Aura.scb"
                    }
                }
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.910002291, 0.910002291, 0.910002291, 0.39000535 }
                }
                disableBackfaceCull: bool = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 2, 0.75 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1.10000002, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Yone_Skin35_Noise_Ink_Edgy_Aura.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1.5, 0.5 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Yone_Skin35_Mask_Edge_Vertical_Edgy_Aura.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3000
                }
                lifetime: option[f32] = {
                    3000
                }
                isSingleParticle: flag = true
                emitterName: string = "up_glow1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -15, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Yone_Skin35_Cylinder_02_Edgy_Aura.scb"
                    }
                }
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.910002291, 0.910002291, 0.910002291, 0.669993162 }
                }
                disableBackfaceCull: bool = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.75, 2, 0.75 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1.10000002, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Yone_Skin35_Streaks_Vertical_Edgy_Aura.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/vfxhub/Yone_Skin35_E_Smoke_Palette_Edgy_Aura.dds"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                    PaletteUAnimationCurve: embed = ValueFloat {
                        constantValue: f32 = 2
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                2
                            }
                        }
                    }
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0199999996, 0.300000012 }
                }
                texAddressModeBase: u8 = 1
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.75, 1 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Yone_Skin35_Mask_Edge_Vertical_Edgy_Aura.dds"
                }
            }
        }
        particleName: string = "Edgy Aura"
        particlePath: string = "Edgy Aura"
    }

# VFX_HUB_NAME: Shadow Aura
# VFX_HUB_DESCRIPTION: Shadow Aura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 4
    "Shadow Aura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    3000
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Ray"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    birthTranslation: embed = ValueVector3 {}
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.43921569, 0.0392156877, 0.0392156877, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.43921569, 0.0392156877, 0.0392156877, 0 }
                            { 0.43921569, 0.0392156877, 0.0392156877, 1 }
                            { 0.43921569, 0.0392156877, 0.0392156877, 0 }
                        }
                    }
                }
                pass: i16 = -15
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 800, 50 }
                }
                texture: string = "ASSETS/vfxhub/udyr_base_vgu_awaken_glow_Shadow_Aura.dds"
                texAddressModeMult: u8 = 2
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    3000
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Ray1"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    birthTranslation: embed = ValueVector3 {}
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.43921569, 0.0392156877, 0.0392156877, 1 }
                }
                pass: i16 = -100
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                depthBiasFactors: vec2 = { 1, 15 }
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 700, 50 }
                }
                texture: string = "ASSETS/vfxhub/udyr_base_vgu_awaken_glow_Shadow_Aura.dds"
                texAddressModeMult: u8 = 2
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    3000
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Ray2"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    birthTranslation: embed = ValueVector3 {}
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.43921569, 0.0392156877, 0.0392156877, 1 }
                }
                pass: i16 = -10
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 600, 50 }
                }
                texture: string = "ASSETS/vfxhub/udyr_base_vgu_awaken_glow_Shadow_Aura.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                }
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "Temp_Ray3"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    birthTranslation: embed = ValueVector3 {}
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.43921569, 0.0392156877, 0.0392156877, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.43921569, 0.0392156877, 0.0392156877, 0 }
                            { 0.43921569, 0.0392156877, 0.0392156877, 1 }
                            { 0.43921569, 0.0392156877, 0.0392156877, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                depthBiasFactors: vec2 = { -1, -50 }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 500, 50 }
                }
                texture: string = "ASSETS/vfxhub/udyr_base_vgu_awaken_glow_Shadow_Aura.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/vfxhub/udyr_base_vgu_awaken_tile03_Shadow_Aura.dds"
                    uvScrollClampMult: flag = true
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.400000006 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                            values: list[vec2] = {
                                { 0, 0.400000006 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            values: list[vec2] = {
                                { 1, 0.5 }
                            }
                        }
                    }
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                                1
                            }
                            values: list[vec2] = {
                                { 1, 0.25 }
                                { 1, 1 }
                            }
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                }
            }
        }
        particleName: string = "Shadow Aura"
        particlePath: string = "Shadow Aura"
    }

# VFX_HUB_NAME: Trail Aura
# VFX_HUB_DESCRIPTION: Trail Aura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 1
    "Trail Aura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 60
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    9.99999988e+26
                }
                emitterName: string = "Pantheon1"
                importance: u8 = 2
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    birthTranslation: embed = ValueVector3 {}
                }
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 700, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.586614192
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0, 0 }
                            { 0.300000012, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Base_Fire_Trail_Graphic_Trail_Aura.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                }
            }
        }
        particleName: string = "Trail Aura"
        particlePath: string = "Trail Aura"
    }

# VFX_HUB_NAME: Udyr Aura
# VFX_HUB_DESCRIPTION: Udyr Aura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 4
    "Udyr Aura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                emitterName: string = "ADD_EdgeGlow"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -25 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
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
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 25, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0x38260b5b
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0509803928, 0.0509803928, 0.0509803928, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.666666687, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.0509803928, 0.0509803928, 0.0509803928, 1 }
                            { 0.0509803928, 0.0509803928, 0.0509803928, 1 }
                            { 0.0509803928, 0.0509803928, 0.0509803928, 1 }
                            { 0.717647076, 0.00392156886, 0.00392156886, 1 }
                        }
                    }
                }
                pass: i16 = 5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.250647753
                                0.59136337
                                1
                            }
                            values: list[f32] = {
                                0
                                0.151515156
                                0.803030312
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Udyr_Base_VGU_Generic_Erosion01_Udyr_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.0500000007
                    fresnelColor: vec4 = { 0.717647076, 0.00392156886, 0.00392156886, 1 }
                }
                depthBiasFactors: vec2 = { 1, 80 }
                stencilMode: u8 = 1
                stencilRef: u8 = 2
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.5, 1.29999995, 1.10000002 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/common_color-hold_Udyr_Aura.dds"
                texDiv: vec2 = { 0.449999988, 0.449999988 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emissionSurfaceDefinition: pointer = VfxEmissionSurfaceData {
                    meshName: string = "ASSETS/vfxhub/sett_Udyr_Aura.skn"
                    skeletonName: string = "ASSETS/vfxhub/sett_Udyr_Aura.skl"
                    meshScale: f32 = 0.800000012
                    useAvatarPose: bool = true
                    useSurfaceNormalForBirthPhysics: bool = false
                }
                emitterName: string = "EF_1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -150 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 3 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
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
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 15, -25 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0509803928, 0.0509803928, 0.0509803928, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.717647076, 0.00392156886, 0.00392156886, 0 }
                            { 0.717647076, 0.00392156886, 0.00392156886, 1 }
                            { 0.717647076, 0.00392156886, 0.00392156886, 0.0980392173 }
                            { 0.0509803928, 0.0509803928, 0.0509803928, 0 }
                        }
                    }
                }
                pass: i16 = 8000
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.250647753
                                0.59136337
                                1
                            }
                            values: list[f32] = {
                                0
                                0.151515156
                                0.803030312
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Udyr_Base_VGU_Generic_Erosion01_Udyr_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -90 }
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 150, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 0.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Udyr_Base_VGU_Awaken_Glow_Udyr_Aura.dds"
                UvRotationMult: embed = ValueFloat {
                    constantValue: f32 = 90
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/vfxhub/Udyr_Base_VGU_Awaken_Tile03_Udyr_Aura.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.200000003 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                            values: list[vec2] = {
                                { 0, 0.200000003 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emissionSurfaceDefinition: pointer = VfxEmissionSurfaceData {
                    meshName: string = "ASSETS/vfxhub/sett_Udyr_Aura.skn"
                    skeletonName: string = "ASSETS/vfxhub/sett_Udyr_Aura.skl"
                    meshScale: f32 = 0.800000012
                    useAvatarPose: bool = true
                    useSurfaceNormalForBirthPhysics: bool = false
                }
                emitterName: string = "EF_1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -150 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 3 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
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
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 15, -25 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0509803928, 0.0509803928, 0.0509803928, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.0509803928, 0.0509803928, 0.0509803928, 0 }
                            { 0.717647076, 0.00392156886, 0.00392156886, 1 }
                            { 0.717647076, 0.00392156886, 0.00392156886, 0.0980392173 }
                            { 0.717647076, 0.00392156886, 0.00392156886, 0 }
                        }
                    }
                }
                pass: i16 = 8000
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.250647753
                                0.59136337
                                1
                            }
                            values: list[f32] = {
                                0
                                0.151515156
                                0.803030312
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Udyr_Base_VGU_Generic_Erosion01_Udyr_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -90 }
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 150, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 0.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Udyr_Base_VGU_Awaken_Glow_Udyr_Aura.dds"
                UvRotationMult: embed = ValueFloat {
                    constantValue: f32 = 90
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/vfxhub/Udyr_Base_VGU_Awaken_Tile03_Udyr_Aura.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.200000003 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                            values: list[vec2] = {
                                { 0, 0.200000003 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.400000006
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    200
                }
                isSingleParticle: flag = true
                emitterName: string = "Cylinder_Blue"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Samira_Skin30_Z_PKCeleb_ArenaFire.PIE_C_13_14_Udyr_Aura.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 200
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 60
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.274545461
                                0.628609717
                                0.845117867
                                0.998310804
                            }
                            values: list[f32] = {
                                0.0272373538
                                0.0272373538
                                0.334431738
                                0.894018054
                                1.00251842
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/vfxhub/Base_mask_18l.PIE_C_13_14_Udyr_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                stencilMode: u8 = 3
                stencilRef: u8 = 3
                birthRotation0: embed = ValueVector3 {
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
                                    0
                                    360
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.13, 5, 1.13 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.13, 5, 1.13 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.25, 0.25, 0.25 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.0250000004, 0, 0.0250000004 }
                            { 0.224999994, 0.125, 0.224999994 }
                            { 0.25, 0.25, 0.25 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/DefaultColorOverlifetime_Udyr_Aura.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.5, 0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.5, 0.300000012 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 5, 1 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/vfxhub/Samira_Skin30_Z_PK_Fire.PIE_C_13_14_Udyr_Aura.dds"
                    uvScaleMult: embed = ValueVector2 {
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        2
                                        3
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "Udyr Aura"
        particlePath: string = "Udyr Aura"
    }

# VFX_HUB_NAME: Spirit Blossom Aura
# VFX_HUB_DESCRIPTION: Spirit Blossom Aura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 12
    "Spirit Blossom Aura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "Sword_Mid_GlowLargeAF"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, -4 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -40, 5 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.650980413, 0.513725519, 0.960784316, 0.970000744 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 130, 1 }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin20_R_Glow_Spirit_Blossom_Aura.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "Sword_Mid_GlowLargeAF1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, -4 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -40, 5 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.650980413, 0.513725519, 0.960784316, 0.889997721 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 12
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 130, 1 }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin20_R_Glow_Spirit_Blossom_Aura.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "Sword_Mid_GlowLargeAF2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, -4 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -50, 10 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.188235298, 0.117647059, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 12
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 75, 230, 1 }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin20_R_Glow_Spirit_Blossom_Aura.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                lifetime: option[f32] = {
                    999999
                }
                isSingleParticle: flag = true
                emitterName: string = "FWOOSH"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -60, 2 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Riven_Skin23_R_Sword01_Spirit_Blossom_Aura.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                pass: i16 = 15
                particleIsLocalOrientation: flag = false
                doesCastShadow: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2.4000001, 2, 2.0999999 }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin23_Z_color-hold_Spirit_Blossom_Aura.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/vfxhub/Riven_Skin23_Z_GradientMult_Spirit_Blossom_Aura.dds"
                    texAddressModeMult: u8 = 2
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { -4, 0 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.899999976, 0 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.850000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "SmolFlames"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -80, 2 }
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
                                { 0, -80, 2 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 10 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
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
                    erosionMapName: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameErosion_Spirit_Blossom_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = false
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 90, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 50, 80, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameQuads_Spirit_Blossom_Aura.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.850000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "HandlePlume"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -30, 2 }
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
                                { 0, -30, 2 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 10 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0784313753, 0.0431372561, 0.352941185, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0.650980413, 0.513725519, 0.960784316, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                            values: list[f32] = {
                                0.400000006
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameErosion_Spirit_Blossom_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = false
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 90, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 60, 80, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameQuads_Spirit_Blossom_Aura.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.899999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.850000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.899999976
                        }
                    }
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "BackgroundFlames"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 2 }
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
                                { 0, 20, 2 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -60, 10 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0784313753, 0.0431372561, 0.352941185, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.650980413, 0.513725519, 0.960784316, 0 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                            values: list[f32] = {
                                0.400000006
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameErosion_Spirit_Blossom_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = false
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, -90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.50999999
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 80, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.699999988, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameQuads_Spirit_Blossom_Aura.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 13
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.550000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.850000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.550000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "Pieces"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -50, 2 }
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
                                { 0, -50, 2 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 10 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0784313753, 0.0431372561, 0.352941185, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0.650980413, 0.513725519, 0.960784316, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.400000006
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameErosion_Spirit_Blossom_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 90, 1 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 50, 80, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameQuads_Spirit_Blossom_Aura.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.899999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.850000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.899999976
                        }
                    }
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "BackgroundFlames1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 2 }
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
                                { 0, 10, 2 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -60, 10 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0666666701, 0.0352941193, 0.31764707, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.650980413, 0.513725519, 0.960784316, 0 }
                            { 0, 0, 0, 1 }
                            { 0.650980413, 0.513725519, 0.960784316, 1 }
                            { 0.650980413, 0.513725519, 0.960784316, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                            values: list[f32] = {
                                0.400000006
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameErosion_Spirit_Blossom_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = false
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.50999999
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 80, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.699999988, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameQuads_Spirit_Blossom_Aura.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.850000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "HandlePlume1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -5, -30, 2 }
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
                                { -5, -30, 2 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 10 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0784313753, 0.0431372561, 0.352941185, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.650980413, 0.513725519, 0.960784316, 0 }
                            { 0, 0, 0, 1 }
                            { 0.650980413, 0.513725519, 0.960784316, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 12
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                            values: list[f32] = {
                                0.400000006
                                0.300000012
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameErosion_Spirit_Blossom_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = false
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 90, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 50, 80, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameQuads_Spirit_Blossom_Aura.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.899999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.850000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.899999976
                        }
                    }
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "BackgroundFlames"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 20, 2 }
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
                                { 0, 20, 2 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -60, 10 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0784313753, 0.0431372561, 0.352941185, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                            values: list[f32] = {
                                0.400000006
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameErosion_Spirit_Blossom_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = false
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, -90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.50999999
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 80, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.699999988, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameQuads_Spirit_Blossom_Aura.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.850000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    999999
                }
                emitterName: string = "SmolFlames"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -80, 2 }
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
                                { 0, -80, 2 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 1.00000012, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 10 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
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
                    erosionMapName: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameErosion_Spirit_Blossom_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = false
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 90, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 50, 80, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Riven_Skin23_Z_FlameQuads_Spirit_Blossom_Aura.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
            }
        }
        particleName: string = "Spirit Blossom Aura"
        particlePath: string = "Spirit Blossom Aura"
    }

# VFX_HUB_NAME: Stars Aura
# VFX_HUB_DESCRIPTION: Stars Aura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 1
    "Stars Aura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Back_Stars1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    Size: vec3 = { 35, 35, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.182539687
                            0.420634925
                            0.750957847
                            1
                        }
                        values: list[vec4] = {
                            { 0.858823538, 0.0235294122, 0.105882354, 0 }
                            { 0.858823538, 0.0235294122, 0.105882354, 1 }
                            { 0.850980401, 0.270588249, 0.772549033, 1 }
                            { 0.850980401, 0.270588249, 0.772549033, 0.886274517 }
                            { 0.858823538, 0.0235294122, 0.105882354, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
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
                                    -20
                                    20
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -20
                                    20
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
                directionVelocityScale: f32 = 0.00400000019
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.300000012
                            0.349999994
                            0.5
                            0.75
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0, 0 }
                            { 2, 0, 0 }
                            { 1, 0, 0 }
                            { 0.200000003, 0, 0 }
                            { 1, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Syndra_Skin34_Sparker02_Stars_Aura.dds"
                numFrames: u16 = 4
            }
        }
        particleName: string = "Stars Aura"
        particlePath: string = "Stars Aura"
    }

# VFX_HUB_NAME: Pyke Smoke Aura
# VFX_HUB_DESCRIPTION: Pyke Smoke Aura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 5
    "Pyke Smoke Aura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    0.699999988
                                    1.10000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                emitterName: string = "Sparks2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -100, -10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
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
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -100, -10, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 3, 2 }
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
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -70, 0, 7 }
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
                                        2
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -70, 0, 7 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 15 }
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
                                { 2, 0, 15 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00600000005
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.600000024
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                            { 0, 0.0117647061, 0.0313725509, 1 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.160006106 }
                        }
                    }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/vfxhub/Pyke_Skin44_Erosion_01_Pyke_Smoke_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -20, -60 }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    350
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 0, 0 }
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
                            { 100, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 28, 56, 4 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.100000001
                                    0.5
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    1
                                    0.5
                                }
                            }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 28, 56, 4 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.600000024, 1 }
                            { 1.5, 1, 1 }
                            { 2, 1.5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Pyke_Skin44_W_GalaxyTwirl_Z01_Pyke_Smoke_Aura.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Pyke_Skin44_Vertical_Mask_Z02_Pyke_Smoke_Aura.dds"
                    texDivMult: vec2 = { 2, 2 }
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 0.5 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.300000012 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                            values: list[vec2] = {
                                { 0, 0.300000012 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.39999998
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.39999998
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "darkMist"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -200, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
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
                            { -200, 40, 40 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
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
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -65, 4, 0 }
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
                                        2
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -65, 4, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 0, 38 }
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
                                { 10, 0, 38 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00600000005
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.972549021 }
                            { 0, 0.0117647061, 0.0313725509, 0.710002303 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                        }
                    }
                }
                pass: i16 = -81
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/vfxhub/Pyke_Skin44_1Q_SmokeErode_Pyke_Smoke_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
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
                            { 1, 90, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 86, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 86, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.702205896, 0.702205896 }
                            { 0.75, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Pyke_Skin44_Sl_Dust_01_02_Pyke_Smoke_Aura.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.39999998
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    1.10000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.39999998
                        }
                    }
                }
                emitterName: string = "Star"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
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
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -100, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
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
                            { -100, 40, 40 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
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
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -70, 0, 0 }
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
                                        2
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -70, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 0, 30 }
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
                                { 20, 0, 30 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00600000005
                }
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0, 0.0117647061, 0.0313725509, 0.560006082 }
                            { 0, 0.0117647061, 0.0313725509, 0.7400015 }
                        }
                    }
                }
                pass: i16 = 28
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -60 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 0 }
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
                            { 400, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 20, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.70000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 7, 20, 10 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.699999988, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Pyke_Skin44_Ash_Pyke_Smoke_Aura.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "darkMist1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -200, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
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
                            { -200, 40, 40 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
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
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -30, 4, 0 }
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
                                        2
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -30, 4, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 0, 28 }
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
                                { 10, 0, 28 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00600000005
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.300007641 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0, 0.0117647061, 0.0313725509, 0.850980401 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.400000006 }
                            { 0, 0.0117647061, 0.0313725509, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/vfxhub/Pyke_Skin44_1Q_SmokeErode_Pyke_Smoke_Aura.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
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
                            { 1, 90, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 80, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.702205896, 0.702205896 }
                            { 0.75, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Pyke_Skin44_Sl_Dust_01_02_Pyke_Smoke_Aura.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.39999998
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    1.10000002
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.39999998
                        }
                    }
                }
                emitterName: string = "Star1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.100000001, 0 }
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
                            { 0, 0.100000001, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -100, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
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
                            { -100, 40, 40 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
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
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { -90, 0, 0 }
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
                                        2
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -90, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 0, 30 }
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
                                { 20, 0, 30 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00600000005
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.788235307, 0.788235307, 0.788235307, 1 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.699999988
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0, 0.0117647061, 0.0313725509, 0.820004582 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.7400015 }
                        }
                    }
                }
                pass: i16 = 68
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -20 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 0 }
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
                            { 400, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 20, 10 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.79999995
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 7, 20, 10 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.699999988, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Pyke_Skin44_Ash_Pyke_Smoke_Aura.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Pyke Smoke Aura"
        particlePath: string = "Pyke Smoke Aura"
    }












     "Characters/Aurora/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "cherryblossomauravfx" = "cherryblossomauravfx"
            "testauravfx" = "testauravfx"
            "fireidle" = "fireidle"
            "Electricity" = "Electricity"
            "Storm Aura" = "Storm Aura"
            "Hand Flames Aura" = "Hand Flames Aura"
            "Edgy Aura" = "Edgy Aura"
            "Shadow Aura" = "Shadow Aura"
            "Trail Aura" = "Trail Aura"
            "Udyr Aura" = "Udyr Aura"
            "Spirit Blossom Aura" = "Spirit Blossom Aura"
            "Stars Aura" = "Stars Aura"
            "Pyke Smoke Aura" = "Pyke Smoke Aura"
        }
     }
} 
