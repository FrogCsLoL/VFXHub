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

# VFX_HUB_NAME: Final Form
# VFX_HUB_DESCRIPTION: Final Form
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 32
    "Final Form" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLinger: option[f32] = {
                    10.1999998
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Add_InitialFlash"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.843137264, 0.43921569, 1 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0.905882359, 0.674509823, 1 }
                            { 1, 0.76000613, 0.379995435, 1 }
                        }
                    }
                }
                pass: i16 = 600
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 110, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 2 }
                            { 2.5, 2.5, 1.83087254 }
                            { 0.699999988, 0.699999988, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Zeri_Skin19_W_Flash01.TFT_Set_7_5_Revival_Final_Form.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLingerType: u8 = 1
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Alpha_Ground"
                Linger: pointer = VfxLingerDefinitionData {
                    UseSeparateLingerColor: flag = true
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.340001523, 0.190005347, 0.00999465957, 1 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[vec4] = {
                                { 0.340001523, 0.190005347, 0.00999465957, 1 }
                                { 0.340001523, 0.190005347, 0.00999465957, 0.480003059 }
                                { 0.340001523, 0.190005347, 0.00999465957, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.340001523, 0.190005347, 0.00999465957, 0.700007617 }
                }
                pass: i16 = -20
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 150, 50 }
                }
                texture: string = "ASSETS/vfxhub/TFT6_Trait_YordleLord_Samira_Base_Alpha_Backdrop_64_Final_Form.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLingerType: u8 = 1
                particleLinger: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Add_Ground"
                Linger: pointer = VfxLingerDefinitionData {
                    UseSeparateLingerColor: flag = true
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.97999543, 0.540001512, 0.160006106, 0.200000003 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.0500000007
                                0.5
                                1
                            }
                            values: list[vec4] = {
                                { 0.97999543, 0.540001512, 0.160006106, 0.200000003 }
                                { 0.97999543, 0.540001512, 0.160006106, 0.200000003 }
                                { 0.627191067, 0.345597684, 0.102402933, 0.0320012197 }
                                { 0.534926295, 0.282282323, 0.0836421624, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.521568656, 0.243137255, 1, 1 }
                }
                pass: i16 = -19
                alphaRef: u8 = 1
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 150, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.850000024
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
                            { 400, 150, 50 }
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
                            { 0.5, 0.5, 0 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/TFT6_Trait_YordleLord_Samira_Base_Alpha_Backdrop_64_Final_Form.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.54999995
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    4
                }
                isSingleParticle: flag = true
                emitterName: string = "Mesh_LightSwirl"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 75, 0 }
                }
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
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Brand_Skin05_Particles_1_9_Final_Form.scb"
                    }
                }
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.760784328 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.900007606, 0.540001512, 0 }
                            { 0.823529422, 0.313725501, 0.737254918, 0.760784328 }
                            { 0.671442747, 0.28731212, 0.0225833524, 0.760784328 }
                            { 0.2399939, 0.2399939, 0.300007641, 0.311917514 }
                            { 0.239215687, 0.239215687, 0.298039228, 0 }
                        }
                    }
                }
                pass: i16 = 2500
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0.800000012
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Leona_Skin21_Particles_1_12_Final_Form.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
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
                                    360
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
                            { 2, 2, 2 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.29999995, 1.20000005, 1.29999995 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
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
                            { 1.29999995, 1.20000005, 1.29999995 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.850000024, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.425000012, 0.5, 0.5 }
                            { 0.764999986, 0.899999976, 0.899999976 }
                            { 1.01999998, 0.5, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Leona_Skin21_Particles_1_15_Final_Form.tex"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 0.699999988, 0 }
                            { 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0199999996
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
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                emitterLinger: option[f32] = {
                    4
                }
                emitterName: string = "Alpha_SparksUp_Dark"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 350, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 350, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
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
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 70
                    height: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00600000005
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.220004573, 0.11999695, 0.00999465957, 0.800000012 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.262745112, 0.0431372561, 0.00784313772, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 25
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 10, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 2, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/TFT_Samira_Base_Throw_Sparks_Final_Form.tex"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, -1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.00999999978
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
                                    0.100000001
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
                    11
                }
                lifetime: option[f32] = {
                    4
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "Add_BurstSparks"
                importance: u8 = 0
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
                    constantValue: vec3 = { 300, 300, -800 }
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
                                    -0.200000003
                                    1
                                }
                            }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 300, -800 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 2, 4 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 550, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 550, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 7
                    height: f32 = 2
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                Color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.736049414, 0.196505681, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.736049414, 0.196505681, 1 }
                            { 1, 0.367783248, 0, 1 }
                        }
                    }
                }
                pass: i16 = 20
                censorModulateValue: vec4 = { 0, 1, 1, 1 }
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
                    constantValue: vec3 = { 18, 18, 18 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 18, 18, 18 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Olaf_Skin16_Sparks_Final_Form.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "Add_SmokeRibbon"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
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
                primitive: pointer = VfxPrimitiveRay {}
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.0399938971, 0.250003815, 0.400000006 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.37000075, 0.39000535, 0.420004576, 1 }
                            { 0.149996191, 0.149996191, 0.160006106, 0 }
                        }
                    }
                }
                pass: i16 = 5
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 1, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 222, 622, 50 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 222, 622, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0.75, 0 }
                            { 0.400000006, 1.5, 0.400000006 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Samira_Base_Flare_Ray_Final_Form.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Samira_Base_R_Energy_Ray_Final_Form.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 0.25 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0199999996
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                particleLingerType: u8 = 1
                emitterLinger: option[f32] = {
                    4
                }
                emitterName: string = "Add_SparksUp_Light"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 330, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 330, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
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
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 70
                    height: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00600000005
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.914351106, 0.583352387, 0.428061336, 1 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.453452349, 0.101960786, 0.0454413667, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 25
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 15, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 2, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/TFT_Samira_Base_Throw_Sparks_Final_Form.tex"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, -1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "Alpha_SmokeRibbon"
                importance: u8 = 0
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
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
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.41441977, 0.214587629, 0.0147554744, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.41441977, 0.214587629, 0.0147554744, 0 }
                            { 0.41441977, 0.214587629, 0.0147554744, 1 }
                            { 0.250289708, 0.130311191, 0.0090336334, 1 }
                            { 0.16800648, 0.0869941935, 0.00599405263, 0 }
                        }
                    }
                }
                pass: i16 = 5
                meshRenderFlags: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                }
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 1, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 600, 50 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 600, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0.75, 0 }
                            { 0.400000006, 1.5, 0.400000006 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Samira_Base_Flare_Ray_Final_Form.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Samira_Base_R_Energy_Ray_Final_Form.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 0.25 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLingerType: u8 = 1
                particleLinger: option[f32] = {
                    1.20000005
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "Alpha_Glow"
                importance: u8 = 0
                Linger: pointer = VfxLingerDefinitionData {
                    UseSeparateLingerColor: flag = true
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.674509823, 0.454901963, 0.0352941193, 0.701960802 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[vec4] = {
                                { 0.674509823, 0.454901963, 0.0352941193, 0.701960802 }
                                { 0.414288074, 0.279403597, 0.0216778647, 0.352356791 }
                                { 0.316860586, 0.213696674, 0.0165799148, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
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
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                    scaleEmitOffsetByBoundObjectHeight: f32 = 0.00499999989
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.58431375, 0.352941185, 0.674509823, 0.701960802 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.150000006
                            0.400000006
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.627118647
                                0.88861984
                                1
                            }
                            values: list[f32] = {
                                0
                                0.121951222
                                0.32520324
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Tar_Impact_Erode_Final_Form.tex"
                }
                miscRenderFlags: u8 = 1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 150, 0 }
                }
                texture: string = "ASSETS/vfxhub/TFT6_Trait_Scrap_Glow_Bright_Final_Form.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/RingMult_Final_Form.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.699999988 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLingerType: u8 = 1
                particleLinger: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "Alpha_DarkGlow"
                importance: u8 = 0
                Linger: pointer = VfxLingerDefinitionData {
                    UseSeparateLingerColor: flag = true
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.420004576, 0.170000762, 0, 0.700007617 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[vec4] = {
                                { 0.420004576, 0.170000762, 0, 0.693011284 }
                                { 0.420004576, 0.170000762, 0, 0.210007623 }
                                { 0.420004576, 0.170000762, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.87843138, 0.0784313753, 0.0666666701, 0.701960802 }
                }
                pass: i16 = -10
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 150, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/TFT6_Trait_YordleLord_Samira_Base_Alpha_Backdrop_64_Final_Form.tex"
            }
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
                particleLinger: option[f32] = {
                    11
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 45
                    height: f32 = 80
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 35, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.737254918, 0.470588237, 1 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.800000012
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
                    erosionMapName: string = "ASSETS/vfxhub/Base_ErosionShapes01.Kiwi_Final_Form.tex"
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
                texture: string = "ASSETS/vfxhub/Base_Lightning02.Kiwi_Final_Form.tex"
                numFrames: u16 = 9
                texDiv: vec2 = { 3, 3 }
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
                    0.170000002
                }
                isSingleParticle: flag = true
                emitterName: string = "OutsideRing"
                importance: u8 = 2
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 0.489997715, 0.200000003, 1 }
                            { 0.909803927, 0.172549024, 0.105882354, 0 }
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
                texture: string = "ASSETS/vfxhub/Base_ShockRing.Kiwi_Final_Form.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Trigger_"
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Base_Crater_01.Kiwi_Final_Form.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.7400015, 0.7400015, 0.7400015, 0.250003815 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0399999991
                            0.0700000003
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0, 0, 1 }
                            { 1, 0.792156875, 0.792156875, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
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
                    erosionFeatherIn: f32 = 1
                    erosionFeatherOut: f32 = 1
                    erosionMapName: string = "ASSETS/vfxhub/Dissolve_Cloudy_01.Kiwi_Final_Form.tex"
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.35000002, 1.60000002, 1.35000002 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1.10000002
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.35000002, 1.60000002, 1.35000002 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0250000004
                            0.0599999987
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.5, 0.200000003 }
                            { 1.10000002, 3, 1.10000002 }
                            { 1, 1, 1 }
                            { 1.01999998, 0.400000006, 1.01999998 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Base_Crater_01.Kiwi_Final_Form.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[f32] = {
                            0.5
                            0.125
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 150, 0, 0 }
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
                                { 150, 0, 0 }
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
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
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
                        }
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
                            0.349999994
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.619607866, 0.56078434, 0.56078434, 1 }
                            { 0.454901963, 0.247058824, 0.247058824, 0 }
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
                texture: string = "ASSETS/vfxhub/Base_Dirt.Kiwi_Final_Form.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, -1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 30 }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                Color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.815686285, 0.380392164, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.815686285, 0.380392164, 1 }
                            { 1, 0.815686285, 0.380392164, 0 }
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
                                0
                                2
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Ashe_Base_ground_CrackNoise_mult.Kiwi_Final_Form.tex"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/vfxhub/Base_color-hold.Kiwi_Final_Form.tex"
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.400000006, 0.200000003 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                emitterName: string = "Avatar2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.450003803 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.0784313753, 0.709803939, 0 }
                            { 1, 0.580392182, 0.101960786, 1 }
                            { 1, 0, 0.184313729, 0 }
                        }
                    }
                }
                pass: i16 = 998
                meshRenderFlags: u8 = 0
                alphaRef: u8 = 0
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.0500000007
                    fresnelColor: vec4 = { 0.752941191, 0.0549019612, 0.20784314, 0 }
                }
                0xcb13aff1: f32 = 20
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.04999995, 1.02499998, 1.04999995 }
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
                            { 1.14999998, 1.08000004, 1.14999998 }
                            { 1.39999998, 1.17999995, 1.39999998 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/White.StrawberryRebuild_Final_Form.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    3
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "border"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -2, 0 }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 3
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.100007631, 0.0200045779, 0.0200045779, 1 }
                }
                pass: i16 = 999
                meshRenderFlags: u8 = 0
                alphaRef: u8 = 0
                0xcb13aff1: f32 = 15
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.05999994, 1.02999997, 1.05999994 }
                }
                texture: string = "ASSETS/vfxhub/White.StrawberryRebuild_Final_Form.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.00999999978
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                    2
                }
                emitterName: string = "Add_Sparks1"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2000, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 10, 2 }
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
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                        }
                        values: list[f32] = {
                            1
                            0.100000001
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 150, 0 }
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
                                0.300000012
                            }
                            values: list[vec3] = {
                                { 50, 150, 0 }
                                { 90, 150, 0 }
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
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.152941182, 0.0431372561, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                pass: i16 = 20
                alphaRef: u8 = 0
                isDirectionOriented: flag = true
                isUniformScale: flag = true
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
                isLocalOrientation: flag = false
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 18, 18, 18 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
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
                            { 18, 18, 18 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Base_Eclipse_GlassShapes.Kiwi_Final_Form.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                    2
                }
                emitterName: string = "Add_Sparks2"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2000, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 10, 2 }
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
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                        }
                        values: list[f32] = {
                            1
                            0.100000001
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 150, 0 }
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
                                0.300000012
                            }
                            values: list[vec3] = {
                                { 50, 150, 0 }
                                { 90, 150, 0 }
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
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.639215708, 0.400000006, 1 }
                            { 1, 0, 0, 1 }
                        }
                    }
                }
                pass: i16 = 1500
                alphaRef: u8 = 0
                isUniformScale: flag = true
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 18, 18, 18 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
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
                            { 18, 18, 18 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.11950887
                            0.400000006
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.931034505, 0.931034505, 0.931034505 }
                            { 1, 1, 1 }
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Base_FrostCrystals.Kiwi_Final_Form.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLingerType: u8 = 1
                particleLinger: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "Alpha_DarkGlow1"
                importance: u8 = 0
                Linger: pointer = VfxLingerDefinitionData {
                    UseSeparateLingerColor: flag = true
                    SeparateLingerColor: embed = ValueColor {
                        constantValue: vec4 = { 0.420004576, 0.170000762, 0, 0.700007617 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[vec4] = {
                                { 0.420004576, 0.170000762, 0, 0.693011284 }
                                { 0.420004576, 0.170000762, 0, 0.210007623 }
                                { 0.420004576, 0.170000762, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.880003035, 0.0699931309, 0.289997697, 0.250003815 }
                }
                pass: i16 = 2000
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 150, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/TFT6_Trait_YordleLord_Samira_Base_Alpha_Backdrop_64_Final_Form.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
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
                            0.349999994
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "lightning_RuneWars"
                importance: u8 = 2
                SpawnShape: pointer = VfxShapeCylinder {}
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Base_InWater_Electricity.Kiwi_Final_Form.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.937254906, 0.266666681, 0.356862754, 1 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0500000007
                            0.162288934
                            0.205065668
                            0.265666038
                            0.402487844
                            0.416443229
                            0.460955054
                            0.500147045
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.992743254 }
                            { 1, 1, 1, 0.223529413 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.223529413 }
                            { 1, 1, 1, 0.223529413 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 1005
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.393996239
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/vfxhub/Base_Electricity_erode.Kiwi_Final_Form.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -30 }
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 13, 6, 5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 13, 6, 5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.13320826
                            0.20075047
                            0.349906206
                            0.388367742
                            0.44652909
                            1
                        }
                        values: list[vec3] = {
                            { 0.568000019, 1, 1 }
                            { 1.5, 1, 1 }
                            { 1.00044799, 1, 1 }
                            { 1.00292802, 1, 1 }
                            { 1.5, 1, 1 }
                            { 1.00880003, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Base_Electricity.Kiwi_Final_Form.tex"
                numFrames: u16 = 2
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.899999976 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.899999976 }
                        }
                    }
                }
                texDiv: vec2 = { 2, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1.70000005 }
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
                            0.313320816
                            0.649155736
                            1
                        }
                        values: list[vec2] = {
                            { 0, -1.70000005 }
                            { 0, -1.70000005 }
                            { 0, -0 }
                            { 0, -0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1.5 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Base_Electricity_mask.Kiwi_Final_Form.tex"
                    texAddressModeMult: u8 = 2
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
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
                            0.349999994
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "lightning_RuneWars1"
                importance: u8 = 2
                SpawnShape: pointer = VfxShapeCylinder {}
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Base_InWater_Electricity.Kiwi_Final_Form.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.145098045, 0, 0.0470588244, 1 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0500000007
                            0.162288934
                            0.205065668
                            0.265666038
                            0.402487844
                            0.416443229
                            0.460955054
                            0.500147045
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.992743254 }
                            { 1, 1, 1, 0.223529413 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.223529413 }
                            { 1, 1, 1, 0.223529413 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 1005
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.393996239
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/vfxhub/Base_Electricity_erode.Kiwi_Final_Form.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -30 }
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 14, 5, 6 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 14, 5, 6 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.13320826
                            0.20075047
                            0.349906206
                            0.388367742
                            0.44652909
                            1
                        }
                        values: list[vec3] = {
                            { 0.568000019, 1, 1 }
                            { 1.5, 1, 1 }
                            { 1.00044799, 1, 1 }
                            { 1.00292802, 1, 1 }
                            { 1.5, 1, 1 }
                            { 1.00880003, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Base_Electricity.Kiwi_Final_Form.tex"
                numFrames: u16 = 2
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.899999976 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.899999976 }
                        }
                    }
                }
                texDiv: vec2 = { 2, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1.70000005 }
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
                            0.313320816
                            0.649155736
                            1
                        }
                        values: list[vec2] = {
                            { 0, -1.70000005 }
                            { 0, -1.70000005 }
                            { 0, -0 }
                            { 0, -0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1.5 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Base_Electricity_mask.Kiwi_Final_Form.tex"
                    texAddressModeMult: u8 = 2
                }
            }
        }
        particleName: string = "Final Form"
        particlePath: string = "Final Form"
        soundOnCreateDefault: string = "Play_sfx_Augment_ARAM_FinalForm_buffactivate"
        soundPersistentDefault: string = "Play_sfx_Augment_ARAM_FinalForm_loop"
        flags: u16 = 71
    }

# VFX_HUB_NAME: FireAuraIdle
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 7
    "FireAuraIdle" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                isSingleParticle: flag = true
                emitterName: string = "ground_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 2, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/vfxhub/FireAuraIdle_texture.tex"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.439993888 }
                }
                Color: embed = ValueColor {
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
                pass: i16 = -1
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 180, 180 }
                }
                texture: string = "ASSETS/vfxhub/Trundle_R_Black_Background_FireAuraIdle.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "Trail"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -100, 300, -100 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 300, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                emissionMeshScale: f32 = 0
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 20, 100, 50 }
                }
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
                        mCutoff: f32 = 800
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 4
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0500000007
                            0.200000003
                            0.304023832
                            0.749627411
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.516666651, 0, 1, 1 }
                            { 0.560165584, 0.0899977088, 1, 1 }
                            { 0.239084974, 0, 0.4627451, 1 }
                            { 0.0911764726, 0, 0.176470593, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                depthBiasFactors: vec2 = { 0, -15 }
                isUniformScale: flag = true
                uvScrollClamp: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 10, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5, 0.5, 0.5 }
                            { 0.699999988, 0.699999988, 0.699999988 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Morgana_Base_FirePillar_FireAuraIdle.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1.79999995, 0 }
                }
                emitterUvScrollRate: vec2 = { -1.5, 0 }
            }
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
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
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
                    1
                }
                emitterName: string = "FireBurst"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 60, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 0, 3 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                    radius: f32 = 30
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 20 }
                }
                blendMode: u8 = 4
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0357675105
                            0.180327863
                            0.524590135
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.676169991, 0.330006868, 1, 1 }
                            { 0.65882355, 0.294117659, 1, 1 }
                            { 0.605751634, 0.184313729, 1, 1 }
                            { 0.336339891, 0, 0.650980413, 1 }
                            { 0.11346405, 0, 0.219607845, 0 }
                        }
                    }
                }
                pass: i16 = 50
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                }
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
                    erosionMapName: string = "ASSETS/vfxhub/Trundle_Skin06_Q_SmokeErode_FireAuraIdle.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -2, -500 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 0, 0 }
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
                            { 150, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 35, 35 }
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
                            { 100, 35, 35 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.430330336
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0, 0 }
                            { 0.767213106, 0.767213106, 0.767213106 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Fire_ember_FireAuraIdle.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 2 }
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
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
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
                    1
                }
                emitterName: string = "FireBurst1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 60, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 0, 3 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                    radius: f32 = 30
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 20 }
                }
                blendMode: u8 = 4
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.135618478
                            0.341281682
                            0.800000012
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.676169991, 0.330006868, 1, 0 }
                            { 0.65882355, 0.294117659, 1, 1 }
                            { 0.258954257, 0.0117647061, 0.490196079, 1 }
                            { 0.0871241838, 0, 0.168627456, 1 }
                            { 0.0911764726, 0, 0.176470593, 0 }
                        }
                    }
                }
                pass: i16 = 50
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                }
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
                    erosionMapName: string = "ASSETS/vfxhub/Trundle_Skin06_Q_SmokeErode_FireAuraIdle.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -2, -100 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 0, 0 }
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
                            { 150, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 35, 35 }
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
                            { 100, 35, 35 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.430330336
                            1
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0, 0 }
                            { 0.767213106, 0.767213106, 0.767213106 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Fire_ember_FireAuraIdle.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 4, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1.5
                }
                emitterName: string = "Sparks"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
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
                            { 0, 2, 0 }
                        }
                    }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
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
                            { 0, 300, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 150, 150, 0 }
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
                                0.300000012
                            }
                            values: list[vec3] = {
                                { 75, 150, 0 }
                                { 135, 150, 0 }
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
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                blendMode: u8 = 4
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.515650749
                            1
                        }
                        values: list[vec4] = {
                            { 0.677777767, 0.333333343, 1, 1 }
                            { 0.410000026, 0.160784319, 0.643137276, 1 }
                            { 0.149934649, 0, 0.290196091, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 0, 100 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.349999994
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 200, 0 }
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
                            { 0, 1, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Trundle_Skin06_Embers_FireAuraIdle.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1.5
                }
                emitterName: string = "ash"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
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
                            { 0, 2, 0 }
                        }
                    }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
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
                            { 0, 300, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 150, 150, 0 }
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
                                0.300000012
                            }
                            values: list[vec3] = {
                                { 75, 150, 0 }
                                { 135, 150, 0 }
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
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.101960786, 0.0823529437, 0.129411772, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.106666669, 0.0823529437, 0.129411772, 1 }
                            { 0.106666669, 0.0823529437, 0.129411772, 1 }
                            { 0.106666669, 0.0823529437, 0.129411772, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 0, 200 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 100, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.349999994
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 100, 0 }
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
                            { 0, 1, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Trundle_Skin06_Embers_FireAuraIdle.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.899999976
                }
                particleLinger: option[f32] = {
                    0.899999976
                }
                emitterName: string = "frost_smoke"
                birthVelocity: embed = ValueVector3 {
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
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 110, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 110, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 200, 20 }
                }
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
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.219934657, 0.149019614, 0.286274523, 0.580392182 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.377049178
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                depthBiasFactors: vec2 = { 1, 5 }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -90
                                    90
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    90
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.150000006
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0
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
                            { 3, 3, 3 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 1, 1 }
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
                        values: list[vec3] = {
                            { 120, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Morde_Skin06_Dust_FireAuraIdle.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "FireAuraIdle"
        particlePath: string = "FireAuraIdle"
    }

# VFX_HUB_NAME: SettAura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 27
    "SettAura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.545098066, 0.0274509806, 1, 1 }
                }
                Color: embed = ValueColor {
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
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 250, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 1, 0.5, 0.5 }
                            { 2, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Aura_Self_SettAura.tex"
                startFrame: u16 = 4
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                emitterName: string = "ground_light1"
                disabled: bool = true
                importance: u8 = 2
                Filtering: pointer = VfxEmitterFiltering {
                    keywordsExcluded: list[string] = {
                        "NasusSkin05"
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 50, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.349996179 }
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
                            { 1, 0.333333343, 0.968627453, 0 }
                            { 0.713725507, 0.219607845, 1, 1 }
                            { 0.360784322, 0.0627451017, 0.874509811, 1 }
                            { 0.0274509806, 0.0784313753, 0.407843143, 0 }
                        }
                    }
                }
                pass: i16 = -101
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -75 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 100, 1 }
                }
                texture: string = "ASSETS/vfxhub/Aura_Self_SettAura.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.454901963, 0.137254909, 1, 0.501960814 }
                }
                Color: embed = ValueColor {
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
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -75 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 250, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 2, 0.5, 0.5 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Aura_Self_SettAura.tex"
                startFrame: u16 = 4
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                blendMode: u8 = 4
                Color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.250980407, 0.611764729, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.250980407, 0.611764729, 0 }
                            { 1, 0.250980407, 0.611764729, 1 }
                            { 1, 0.250980407, 0.611764729, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -75 }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 250, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.5, 0.5 }
                            { 0.5, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Aura_Self_SettAura.tex"
                startFrame: u16 = 4
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.349996179 }
                }
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.164705887, 0.0431372561, 0.482352942, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.164705887, 0.0431372561, 0.482352942, 0 }
                            { 0.164705887, 0.0431372561, 0.482352942, 1 }
                            { 0.164705887, 0.0431372561, 0.482352942, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 250, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.5, 0.5 }
                            { 0.75, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Aura_Self_SettAura.tex"
                startFrame: u16 = 4
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
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
                                    0.300000012
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
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Variant_Burst"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
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
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Sett_Skin38_W_SwooshMesh_SettAura.scb"
                    }
                }
                blendMode: u8 = 1
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.0549019612, 0.0313725509, 0.223529413, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0549019612, 0.0313725509, 0.223529413, 1 }
                            { 0.0549019612, 0.0313725509, 0.223529413, 1 }
                            { 0.0549019612, 0.0313725509, 0.223529413, 0 }
                        }
                    }
                }
                pass: i16 = 999
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/vfxhub/Sett_Skin20_R_Wisps_SettAura.tex"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
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
                            { 360, 360, 360 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 0.629999995, 0.629999995 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0, 0 }
                            { 1, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_W_Dot_SettAura.tex"
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec2] = {
                            { 2, 0 }
                            { 0.100000001, 0 }
                            { 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
                                    1.25
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
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
                                    0.699999988
                                    2
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
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Variant_Cont"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
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
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Sett_Skin38_W_SwooshMesh_SettAura.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.710002303 }
                }
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.0549019612, 0.0313725509, 0.223529413, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0549019612, 0.0313725509, 0.223529413, 0 }
                            { 0.0549019612, 0.0313725509, 0.223529413, 1 }
                            { 0.0549019612, 0.0313725509, 0.223529413, 0.76000613 }
                            { 0.0549019612, 0.0313725509, 0.223529413, 0 }
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
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/vfxhub/Sett_Skin20_R_Wisps_SettAura.tex"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
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
                            { 360, 360, 360 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 0.629999995, 0.629999995 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0, 0 }
                            { 1, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_W_Dot_SettAura.tex"
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec2] = {
                            { 0.5, 0 }
                            { 0.0250000004, 0 }
                            { 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.64999998
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2.5
                        }
                    }
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
                                    0.699999988
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
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Variant_Cont1"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 250, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Sett_Skin38_W_SwooshMesh_SettAura.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.420004576 }
                }
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.0549019612, 0.0313725509, 0.223529413, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0549019612, 0.0313725509, 0.223529413, 0 }
                            { 0.0549019612, 0.0313725509, 0.223529413, 1 }
                            { 0.0549019612, 0.0313725509, 0.223529413, 1 }
                            { 0.0549019612, 0.0313725509, 0.223529413, 0 }
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
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/vfxhub/Sett_Skin20_R_Wisps_SettAura.tex"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
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
                            { 360, 360, 360 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 0.629999995, 0.629999995 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0, 0 }
                            { 1, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_W_Dot_SettAura.tex"
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec2] = {
                            { 0.400000006, 0 }
                            { 0.0199999996, 0 }
                            { 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "ground_Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.280003041, 0.0200045779, 0.500007629, 1 }
                }
                pass: i16 = -25
                meshRenderFlags: u8 = 0
                colorLookUpScales: vec2 = { 1, 0.400000006 }
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 45, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 200, 200 }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_VGU_Awaken_Glow_SettAura.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Ray"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0, 1, 1 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -15
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 800, 50 }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_VGU_Awaken_Glow_SettAura.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    texAddressModeMult: u8 = 2
                    uvScrollClampMult: flag = true
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "ground_Glow1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.588235319, 0.0117647061, 1, 1 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -30
                meshRenderFlags: u8 = 0
                colorLookUpScales: vec2 = { 1, 0.400000006 }
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -75 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 45, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 350, 200, 200 }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_VGU_Awaken_Glow_SettAura.tex"
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
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Ray1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.580392182, 0.0627451017, 1, 1 }
                }
                pass: i16 = -100
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                depthBiasFactors: vec2 = { 1, -55 }
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 700, 50 }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_VGU_Awaken_Glow_SettAura.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    texAddressModeMult: u8 = 2
                    uvScrollClampMult: flag = true
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
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Ray2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0.500007629, 1 }
                }
                pass: i16 = -10
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 600, 50 }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_VGU_Awaken_Glow_SettAura.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0705882385, 0.105882354, 0.223529413, 1 }
                }
                Color: embed = ValueColor {
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
                    constantValue: vec3 = { 300, 650, 50 }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_VGU_Awaken_Glow_SettAura.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Sett_Skin38_VGU_Awaken_Tile03_SettAura.tex"
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
                }
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
                emitterName: string = "Distort_FAST"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 40, 0 }
                }
                particleColorTexture: string = "ASSETS/vfxhub/SettAura_texture.tex"
                blendMode: u8 = 1
                pass: i16 = 2
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.00999999978
                    normalMapTexture: string = "ASSETS/vfxhub/distort-pinch_SettAura.tex"
                }
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 175, 175 }
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
                texture: string = "ASSETS/vfxhub/Aura_Self_SettAura.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Distort"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/vfxhub/SettAura_texture.tex"
                blendMode: u8 = 1
                Color: embed = ValueColor {
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
                    normalMapTexture: string = "ASSETS/vfxhub/Gragas_Skin10_Z_Circle_normal_SettAura.tex"
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
                texture: string = "ASSETS/vfxhub/color-hold_SettAura.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.180000007
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "DistortFAST"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/vfxhub/SettAura_texture.tex"
                blendMode: u8 = 1
                Color: embed = ValueColor {
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
                    normalMapTexture: string = "ASSETS/vfxhub/Gragas_Skin10_Z_Circle_normal_SettAura.tex"
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
                texture: string = "ASSETS/vfxhub/color-hold_SettAura.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 35
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
                particleLinger: option[f32] = {
                    1
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
                SpawnShape: pointer = VfxShapeLegacy {
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
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.737254918, 0.611764729, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.737254918, 0.611764729, 1, 1 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.619607866, 0.56078434, 0.56078434, 1 }
                            { 0.454901963, 0.247058824, 0.247058824, 0 }
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
                    constantValue: vec3 = { 30, 30, 0 }
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
                            { 30, 30, 0 }
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
                texture: string = "ASSETS/vfxhub/Sett_Skin38_W_Dirt_SettAura.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, -1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 30 }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "Hair_Mat"
                            "Ezreal_Base_Mat"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.590005338 }
                }
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.262745112, 0.741176486, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.262745112, 0.741176486, 1, 1 }
                            { 0.262745112, 0.741176486, 1, 0 }
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
                                0
                                2
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Sett_Ashe_Skin38_ground_CrackNoise_mult_SettAura.tex"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/vfxhub/color-hold_SettAura.tex"
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.400000006, 0.200000003 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.0599999987
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar_Black"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 30 }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "Hair_Mat"
                            "Ezreal_Base_Mat"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.669993162 }
                }
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.200000003, 0, 0, 1 }
                }
                pass: i16 = 1000
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/vfxhub/color-hold_SettAura.tex"
                numFrames: u16 = 4
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.400000006, 0.200000003 }
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
                emitterName: string = "Temp_Ray4"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.662745118, 0.388235301, 1, 1 }
                }
                Color: embed = ValueColor {
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
                pass: i16 = 10
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                depthBiasFactors: vec2 = { -1, -90 }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 350, 650, 50 }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_VGU_Awaken_Glow_SettAura.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Sett_Skin38_VGU_Awaken_Tile03_SettAura.tex"
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
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1.64999998
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
                                    0.699999988
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
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Variant_Cont2"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 250, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Sett_Skin38_W_SwooshMesh_SettAura.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.289997697 }
                }
                Color: embed = ValueColor {
                    constantValue: vec4 = { 0.956862748, 0.470588237, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.956862748, 0.470588237, 1, 0 }
                            { 0.956862748, 0.470588237, 1, 1 }
                            { 0.956862748, 0.470588237, 1, 1 }
                            { 0.956862748, 0.470588237, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.349999994
                    erosionFeatherOut: f32 = 0.349999994
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/vfxhub/Sett_Skin20_R_Wisps_SettAura.tex"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
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
                            { 360, 360, 360 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 0.629999995, 0.629999995 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.581132114, 0, 0 }
                            { 1, 0, 0 }
                            { 1.20000005, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_W_Dot_SettAura.tex"
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec2] = {
                            { 0.400000006, 0 }
                            { 0.0199999996, 0 }
                            { 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 18
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                emitterName: string = "FrontAura"
                Filtering: pointer = VfxEmitterFiltering {
                    keywordsExcluded: list[string] = {
                        "NasusSkin05"
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 250, 0 }
                        }
                    }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 35
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -60, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.80392158, 0.156862751, 1, 1 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.770000756, 0.820004582, 1, 0.910002291 }
                            { 0.56078434, 0.58431375, 1, 0 }
                        }
                    }
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 200, 100 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.39999998, 1.5, 1.20000005 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00326527096
                            0.165097401
                            0.302352458
                            0.458148032
                            0.613560498
                            0.753609896
                            0.99206984
                        }
                        values: list[vec3] = {
                            { 0.952000022, 0.618773937, 0.246153861 }
                            { 1.12, 0.72403574, 0.246153861 }
                            { 1.51643443, 1.02621984, 0.246153861 }
                            { 1.80942571, 1.26807594, 0.246153861 }
                            { 1.68955088, 1.31333995, 0.246153861 }
                            { 1.39573002, 1.2750268, 0.246153861 }
                            { 1.25999999, 1.20000005, 0.278986514 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_Mist_Noise_SettAura.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Sett_Skin38_Particles_1_513_SettAura.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
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
                                        0
                                    }
                                }
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
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 13
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                emitterName: string = "FrontAura1"
                Filtering: pointer = VfxEmitterFiltering {
                    keywordsExcluded: list[string] = {
                        "NasusSkin05"
                    }
                }
                birthVelocity: embed = ValueVector3 {
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
                                    0.800000012
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
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 25
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -60, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.788235307, 0.450980395, 0.898039222, 0.980392158 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.905882359, 0.827450991, 1, 0.952941179 }
                            { 0.850980401, 0.776470602, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 165, 200, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 165, 200, 100 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.29999995, 1.29999995, 1.29999995 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00326527096
                            0.165097401
                            0.302352458
                            0.458148032
                            0.613560498
                            0.753609896
                            0.99206984
                        }
                        values: list[vec3] = {
                            { 0.884000003, 0.536270738, 0.266666681 }
                            { 1.03999996, 0.627497673, 0.266666681 }
                            { 1.40811765, 0.889390588, 0.266666681 }
                            { 1.68018103, 1.09899926, 0.266666681 }
                            { 1.56886864, 1.13822794, 0.266666681 }
                            { 1.29603493, 1.10502326, 0.266666681 }
                            { 1.16999996, 1.03999996, 0.302235395 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_Mist_Noise_SettAura.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Sett_Skin38_Particles_1_513_SettAura.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
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
                                        0
                                    }
                                }
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
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    0.25
                }
                emitterName: string = "StrokeDissolve_Cast"
                importance: u8 = 2
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
                                    0.75
                                    2
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
                    constantValue: vec3 = { 200, 0, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 0, 2 }
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
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 10
                    height: f32 = 10
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.858823538, 0.137254909, 1, 1 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.97999543, 0.960006118, 0 }
                            { 1, 0.984313726, 0.97647059, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -10
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
                    erosionFeatherIn: f32 = 0.0500000007
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/vfxhub/Sett_Skin38_W_Smoke_2_Erosion_SettAura.tex"
                    erosionMapAddressMode: u8 = 0
                }
                depthBiasFactors: vec2 = { -1, -15 }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -20, 0 }
                }
                isLocalOrientation: flag = false
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.349999994
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.349999994
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 150, 100 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.800000012 }
                            { 0.75, 0.800000012, 0.75 }
                            { 1, 0.899999976, 1 }
                            { 0.899999976, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Sett_Skin38_Mist_Noise_SettAura.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Sett_Skin38_3026Vertical_Mask_Wispy_SettAura.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.300000012, 0 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                emitterName: string = "ground_light2"
                importance: u8 = 2
                Filtering: pointer = VfxEmitterFiltering {
                    keywordsExcluded: list[string] = {
                        "NasusSkin05"
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 200, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.820004582 }
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
                            { 1, 0.333333343, 0.968627453, 0 }
                            { 0.713725507, 0.219607845, 1, 1 }
                            { 0.360784322, 0.0627451017, 0.874509811, 1 }
                            { 0.0274509806, 0.0784313753, 0.407843143, 0 }
                        }
                    }
                }
                pass: i16 = -999
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 230, 100, 1 }
                }
                texture: string = "ASSETS/vfxhub/Aura_Self_SettAura.tex"
            }
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
                    constantValue: vec4 = { 1, 0.0800030529, 0.349996179, 0.659998477 }
                }
                Color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.25
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.0823529437, 0, 1, 1 }
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
                texture: string = "ASSETS/vfxhub/Jhin_base_Rose_petals_SettAura.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "SettAura"
        particlePath: string = "SettAura"
    }

# VFX_HUB_NAME: NimbleFootAura
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 16
    "NimbleFootAura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                emitterName: string = "Basic1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                    radius: f32 = 45
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0705882385, 0.0705882385, 0.0705882385, 0.680003047 }
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
                pass: i16 = -5
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 170, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
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
                            { 150, 170, 0 }
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
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_MisGlow_NimbleFootAura.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_SmokeA_NimbleFootAura.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 3 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
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
                                    0.200000003
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
                emitterName: string = "BurstSparks1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
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
                            { 0, 2, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 70, 200 }
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
                                    10
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 70, 200 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 45, 2, 45 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.454901963, 0.0941176489, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                        }
                    }
                }
                pass: i16 = 35
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                directionVelocityScale: f32 = 0.00800000038
                directionVelocityMinScale: f32 = 1.29999995
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 20, 0 }
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
                            { 10, 20, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1.29999995, 0 }
                            { 0.100000001, 0.100000001, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Spark_tar_NimbleFootAura.tex"
                numFrames: u16 = 2
                texDiv: vec2 = { 2, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Conemesh_1"
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_AnimeBurstMesh01_NimbleFootAura.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.229999244 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0705882385, 0.0784313753, 0.105882354, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_AnimeShapesMeshErosion_NimbleFootAura.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2.5, 4.5, 2.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.899999976, 0.899999976 }
                            { 1, 1.29999995, 1 }
                            { 1.20000005, 1.29999995, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_AnimeShapesMesh01_NimbleFootAura.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0.5 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1.5, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.119999997
                rate: embed = ValueFloat {
                    constantValue: f32 = 55
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
                                    1
                                    1.39999998
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
                    0.100000001
                }
                emitterName: string = "Dark_Whirlwind2"
                birthVelocity: embed = ValueVector3 {
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
                            { 0, 200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 100, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                0
                            }
                            values: list[vec3] = {
                                { 0, 60.0000038, 0 }
                                { 0, 50, 0 }
                            }
                        }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Helix_NimbleFootAura.sco"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                }
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 280, 100, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 280, 100, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 400, 0 }
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
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 400, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0
                        }
                        values: list[vec3] = {
                            { 8, 8, 8 }
                            { 12, 12, 8 }
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
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 0.899999976, 0.899999976, 0.400000006 }
                            { 2, 2, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_AirHelix_TX_NimbleFootAura.tex"
                numFrames: u16 = 4
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.119999997
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
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
                                    1
                                    1.39999998
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
                    0.300000012
                }
                emitterName: string = "Dark_Whirlwind3"
                birthVelocity: embed = ValueVector3 {
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
                            { 0, 200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 100, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                0
                            }
                            values: list[vec3] = {
                                { 0, 60.0000038, 0 }
                                { 0, 50, 0 }
                            }
                        }
                    }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Helix_NimbleFootAura.sco"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.549996197 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                }
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 280, 100, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 280, 100, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 400, 0 }
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
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 400, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0
                        }
                        values: list[vec3] = {
                            { 8, 8, 8 }
                            { 12, 12, 8 }
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
                            { 1, 1, 0.600000024 }
                            { 2, 2, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_AirHelix_TX_NimbleFootAura.tex"
                numFrames: u16 = 4
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                }
                texDiv: vec2 = { 2, 2 }
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
                                    1
                                    2.5
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
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "Ein_1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    height: f32 = 40
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Smoke_Twirl_3_NimbleFootAura.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.890196085, 0.219607845, 0.0862745121, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                        }
                    }
                }
                pass: i16 = 300
                alphaRef: u8 = 0
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
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Heal_Fire_Trail_NimbleFootAura.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -30 }
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 180, 0 }
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
                                    180
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 180, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { -0.600000024, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.29999995
                                }
                            }
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1.29999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -0.600000024, 1, 0.600000024 }
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
                            { 1, 0.899999976, 1 }
                            { 1.60000002, 0.400000006, 1.60000002 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Wisps34_NimbleFootAura.tex"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
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
                            { 0, 1 }
                        }
                    }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.0697807148
                            0.144875035
                            0.206343681
                            0.284523666
                            0.381061733
                            0.559383392
                            0.747436821
                            0.996688724
                        }
                        values: list[vec2] = {
                            { 0, 0.112912387 }
                            { 0, 0.115116172 }
                            { 0, 0.113356642 }
                            { 0, 0.109750733 }
                            { 0, 0.109833211 }
                            { 0, 0.0921698362 }
                            { 0, 0.0668896586 }
                            { 0, 0.0622708946 }
                            { 0, 0.0457752943 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1.5 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Smoke_Twirl_Return_Mult_NimbleFootAura.tex"
                    texAddressModeMult: u8 = 2
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 0.5 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.899999976 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
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
                                    0.25
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
                lifetime: option[f32] = {
                    4
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAttractionDefinitions: list[embed] = {
                        VfxFieldAttractionDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            acceleration: embed = ValueFloat {
                                constantValue: f32 = 200
                            }
                        }
                    }
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 300
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 70
                            }
                            axisFraction: vec3 = { 0.25, 0.5, 0.25 }
                        }
                    }
                }
                emitterName: string = "Embers1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 50
                    height: f32 = 10
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                        }
                    }
                }
                pass: i16 = 25
                depthBiasFactors: vec2 = { -1, -1 }
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                }
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Glow5_NimbleFootAura.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Ground_Dirt_Impact 1"
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0705882385, 0.0705882385, 0.0705882385, 0.368627459 }
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
                pass: i16 = 3
                alphaRef: u8 = 0
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
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Tar_WispMult_NimbleFootAura.tex"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 90 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 1, 90 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 390, 0 }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Explosion_groundBurn_NimbleFootAura.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_TFT_Glb_Gradient_NimbleFootAura.tex"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Ground_Glow_Dark2"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0666666701, 0.0235294122, 0.0235294122, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                        }
                    }
                }
                pass: i16 = -50
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 1, 1 }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Aura_Self_NimbleFootAura.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "Ground_Glow_Dark3"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.439993888 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.505882382, 0.152941182, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                        }
                    }
                }
                pass: i16 = 600
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                }
                depthBiasFactors: vec2 = { -1, -55 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 155, 1, 1 }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Aura_Self_NimbleFootAura.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.119999997
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
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
                            0.400000006
                        }
                    }
                }
                emitterName: string = "Ground_Impact1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 0 }
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
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -20, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec3] = {
                                { 30, 0, 0 }
                                { 50, 0, 0 }
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
                        { 0, 1.00000012, 0 }
                    }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 360, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 375, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 150, 375, 30 }
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
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Smoke_Vert_NimbleFootAura.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1.79999995, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    -0.400000006
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1.79999995, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0.5 }
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
                            { 0.5, 0.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.25
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
                            1.25
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "ShadowWisps2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 10, 10, 10 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -25, 30, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.839993894, 0.269993126, 0.100007631, 0.779995441 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0645756423
                            0.145756453
                            0.249446496
                            0.396678954
                            0.715867162
                            1
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.0974994302 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.70199585 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.779995441 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.714995801 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.149881467 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                        }
                    }
                }
                pass: i16 = 300
                alphaRef: u8 = 1
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 40
                }
                depthBiasFactors: vec2 = { -1, -50 }
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
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
                            { 20, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 100, 30 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.15189302
                            0.288518697
                            0.437978595
                            0.676538765
                            1.01228881
                        }
                        values: list[vec3] = {
                            { 0.493251532, 0.493251532, 0.493251532 }
                            { 0.59179461, 0.599134266, 0.599134266 }
                            { 0.813149452, 0.818178833, 0.818178833 }
                            { 0.899999976, 0.985026121, 0.985026121 }
                            { 1, 1.14744473, 1.12441075 }
                            { 1.10000002, 1.31095934, 1.31095934 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_fog_NimbleFootAura.tex"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
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
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "blast1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 400 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    12
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
                        values: list[vec3] = {
                            { 400, 0, 400 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 15, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    height: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 35, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.325490206, 0.176470593, 0.176470593, 0.709803939 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.449999988
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.709803939 }
                            { 1, 1, 1, 0.475563794 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                        }
                    }
                }
                pass: i16 = -150
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 1.20000005
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1.20000005
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_SmokeErode_NimbleFootAura.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
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
                    constantValue: vec3 = { 50, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 1, 0 }
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
                            { 0.5, 1, 1 }
                            { 1, 2, 2 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Sion_Skin05_Sl_Dust_01_NimbleFootAura.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "mesh_ground3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -30, 0 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00400000019
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_weaponswipe_NimbleFootAura.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.192156866, 0.211764708, 0.290196091, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.600000024 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.190588236 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                        }
                    }
                }
                pass: i16 = -100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.150000006
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Erode_NimbleFootAura.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
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
                                    1
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 1.14999998, 0.400000006 }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Smoke_Trail_NimbleFootAura.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 0 }
                }
                texDiv: vec2 = { 0.5, 1 }
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
                                    1.39999998
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
                    0.5
                }
                emitterName: string = "mesh_ground4"
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
                SpawnShape: pointer = VfxShapeBox {
                    Size: vec3 = { 0, 30, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_weaponswipe6_NimbleFootAura.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
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
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0.670588255 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.25
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_1Q_SmokeErode_NimbleFootAura.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0.125490203, 0.576470613, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
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
                                    1
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 2, 0.5 }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Wisps36_NimbleFootAura.tex"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.300000012, 0 }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 1.29999995, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 0.519999981, 0 }
                            { 0.129999995, 0 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Mult_NimbleFootAura.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 0 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
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
                        values: list[f32] = {
                            2.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "spark_skin1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -10, 700, 10 }
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
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    10
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -10, 700, 10 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 80, 50, 80 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.62999922 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0980392173, 0.113725491, 0.152941182, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 1 }
                            { 0.0705882385, 0.0705882385, 0.0705882385, 0 }
                        }
                    }
                }
                pass: i16 = 5
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                directionVelocityScale: f32 = 0.00800000038
                directionVelocityMinScale: f32 = 1.29999995
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 20, 0 }
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
                            { 40, 20, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0.5, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/PetNimblefoot_Skin6_Emote_Ash_NimbleFootAura.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "NimbleFootAura"
        particlePath: string = "NimbleFootAura"
        flags: u16 = 197
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
            "Final Form" = "Final Form"
            "FireAuraIdle" = "FireAuraIdle"
            "SettAura" = "SettAura"
            "NimbleFootAura" = "NimbleFootAura"
        }
     }
} 
