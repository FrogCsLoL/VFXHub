entries: map[hash,embed] = {

# VFX_HUB_NAME: ass
# VFX_HUB_DESCRIPTION: asss
# VFX_HUB_CATEGORY: auras
# VFX_HUB_EMITTERS: 11
    "ass" =     "Characters/Aurora/Skins/Skin0/Particles/Aurora_Base_Emote_RecallPortal" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
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
                    constantValue: vec3 = { 0, 51, -40 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/aurora_base_q_halfsphere_01.aurora_ass.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.699999988 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.349999994
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.239215687, 0.784313738, 0.905882359, 1 }
                            { 0.294117659, 0.870588243, 1, 1 }
                            { 0.152941182, 0.650980413, 0.760784328, 0 }
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
                                0.200000003
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                0.400000006
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/testvfxchampion_skin06_q_crack_erosion.aurora_ass.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.949999988, 0.100000001, 0.949999988 }
                }
                texture: string = "ASSETS/vfxhub/aurora_passivering01.aurora_ass.tex"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 45
                }
                particleUVRotateRate: embed = IntegratedValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            15
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
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
                    constantValue: vec3 = { 0, 51, -40 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/aurora_base_q_halfsphere_01.aurora_ass.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.349999994
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.501960814, 0.717647076, 0.764705896, 1 }
                            { 0.498039216, 0.909803927, 1, 1 }
                            { 0.305882365, 0.686274529, 0.772549033, 0 }
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
                                0.200000003
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                0.400000006
                                0
                                0
                                0
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/testvfxchampion_skin06_q_crack_erosion.aurora_ass.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.100000001, 0.899999976 }
                }
                texture: string = "ASSETS/vfxhub/aurora_passivering01.aurora_ass.tex"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 45
                }
                birthUvRotateRate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
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
                    constantValue: vec3 = { 0, 51, -40 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/aurora_base_q_halfsphere_01.aurora_ass.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.509803951, 0.909803927, 1, 0.5 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.899999976
                            4
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
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
                                0.200000003
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                0.400000006
                                0
                                0
                                0
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/testvfxchampion_skin06_q_crack_erosion.aurora_ass.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.100000001, 0.899999976 }
                }
                texture: string = "ASSETS/vfxhub/aurora_passivering01.aurora_ass.tex"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 45
                }
                birthUvRotateRate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
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
                            0.300000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "Lightning_AOE_Ring"
                importance: u8 = 2
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
                        mSimpleMeshName: string = "ASSETS/vfxhub/udyr_base_r_roundmesh03.aurora_ass.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.289997697, 0.349996179, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.290196091, 0.870588243, 1, 0.400000006 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.992156863, 1, 1, 0 }
                            { 0.992156863, 1, 1, 1 }
                            { 0.603921592, 0.925490201, 1, 1 }
                            { 0.498039216, 0.909803927, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.216184646
                                1
                            }
                            values: list[f32] = {
                                0.400000006
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/vfxhub/flames_floor.aurora_ass.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.699999988, 0.899999976 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0.699999988, 0.899999976 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 2, 1, 2 }
                            { 1.95000005, 1.5, 1.95000005 }
                            { 2.20000005, 2.20000005, 2.20000005 }
                            { 3, 2, 3 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/gnar_skin22_particles_1_339.aurora_ass.tex"
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.699999988
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
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {}
                emitterName: string = "Portal_Close_Sparks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 300 }
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
                                    0.200000003
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
                            { 300, 300, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 4, 4 }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                            { 0, 0, 0 }
                            { 0, -500, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    4
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
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                        }
                        values: list[f32] = {
                            0
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                    radius: f32 = 40
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -75 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.603921592, 0.925490201, 1, 0.5 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.356862754, 0.670588255, 0.741176486, 0 }
                        }
                    }
                }
                pass: i16 = 3
                colorLookUpTypeX: u8 = 2
                colorLookUpTypeY: u8 = 3
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 25
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 15, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 15, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            0.699999988
                            0.709999979
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 5 }
                            { 1, 2, 1 }
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 1, 1 }
                            { 0.600000024, 0.600000024, 1 }
                            { 0.200000003, 0.5, 1 }
                            { 0.200000003, 0.5, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/vayne_base_taunt_flecks.aurora_ass.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.699999988
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
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    5
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAttractionDefinitions: list[embed] = {
                        VfxFieldAttractionDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 50, -40 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 600
                            }
                            acceleration: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                        }
                    }
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {}
                    }
                }
                emitterName: string = "Portal_Close_Sparks1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
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
                                    0.100000001
                                    2
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
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                        }
                        values: list[f32] = {
                            0
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    radius: f32 = 200
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, -40 }
                }
                particleColorTexture: string = ""
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.500007629 }
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
                            { 0.509803951, 0.909803927, 1, 1 }
                            { 0.309803933, 0.686274529, 0.768627465, 0 }
                        }
                    }
                }
                pass: i16 = 2
                depthBiasFactors: vec2 = { -1, -1 }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 10, 15 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 10, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            0.699999988
                            0.709999979
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 5 }
                            { 2, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 1, 1 }
                            { 0.300000012, 0.600000024, 1 }
                            { 0.5, 0.200000003, 1 }
                            { 0.5, 0.200000003, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/base_generic_sparks_add.aurora_ass.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterName: string = "Glow"
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
                    constantValue: vec3 = { 0, 10, -40 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/aurora_base_q_halfsphere_01.aurora_ass.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.5 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.349999994
                            0.400000006
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.129411772, 0.666666687, 0.788235307, 1 }
                            { 0.254901975, 0.862745106, 1, 1 }
                            { 0.498039216, 0.909803927, 1, 1 }
                            { 0.603921592, 0.925490201, 1, 1 }
                        }
                    }
                }
                pass: i16 = -50
                meshRenderFlags: u8 = 0
                disableBackfaceCull: bool = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.79999995, 0.5, 1.79999995 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/aurora_base_r_backdrop.aurora_ass.tex"
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 45
                }
                particleUVRotateRate: embed = IntegratedValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[f32] = {
                            0
                            0
                            1000
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.699999988
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
                            1
                        }
                    }
                }
                lifetime: option[f32] = {
                    5
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAttractionDefinitions: list[embed] = {
                        VfxFieldAttractionDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 50, -40 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 600
                            }
                            acceleration: embed = ValueFloat {
                                constantValue: f32 = 500
                            }
                        }
                    }
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {}
                    }
                }
                emitterName: string = "Portal_Close_Sparks2"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
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
                                    0.100000001
                                    2
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
                bindWeight: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                        }
                        values: list[f32] = {
                            0
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    radius: f32 = 200
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, -40 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.500007629 }
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
                            { 0.509803951, 0.909803927, 1, 1 }
                            { 0.309803933, 0.686274529, 0.768627465, 0 }
                        }
                    }
                }
                pass: i16 = 2
                depthBiasFactors: vec2 = { -1, -1 }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 0 }
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
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            0.699999988
                            0.709999979
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 5 }
                            { 2, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 1, 1 }
                            { 0.300000012, 0.600000024, 1 }
                            { 0.5, 0.200000003, 1 }
                            { 0.5, 0.200000003, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/base_generic_sparks_add.aurora_ass.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "vortex_cap1"
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
                    constantValue: vec3 = { 0, 50, -40 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/aurora_base_q_halfsphere_01.aurora_ass.scb"
                    }
                }
                particleColorTexture: string = "ASSETS/vfxhub/color-hold.tft_set15_ass.dds"
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0 }
                }
                pass: i16 = -10
                miscRenderFlags: u8 = 1
                stencilMode: u8 = 1
                stencilRef: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.699999988, 0.100000001, 0.699999988 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/aurora_base_emote_portal_cover_black_01.aurora_ass.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "vortex_lines3"
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
                    constantValue: vec3 = { 0, 50, -40 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/aurora_base_emote_portal_mesh_01.aurora_ass.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.129411772, 0.666666687, 0.788235307, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0199999996
                            0.100000001
                            0.300000012
                            0.899999976
                            0.980000019
                            1
                        }
                        values: list[vec4] = {
                            { 0.992156863, 1, 1, 0 }
                            { 0.992156863, 1, 1, 1 }
                            { 0.992156863, 1, 1, 1 }
                            { 0.992156863, 1, 1, 0.600000024 }
                            { 0.992156863, 1, 1, 0.219607845 }
                            { 0.23137255, 0.517647088, 0.58431375, 0 }
                        }
                    }
                }
                pass: i16 = -10
                miscRenderFlags: u8 = 1
                stencilMode: u8 = 2
                stencilRef: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 0.5, 2 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0299999993
                            0.0500000007
                            0.100000001
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.10000002, 0.600000024, 1.10000002 }
                            { 0.949999988, 0.5, 0.949999988 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/flames_floor.aurora_ass.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/vfxhub/aurora_gradient3.aurora_ass.tex"
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 2.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                            { 0, -2.5 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.600000024, 0.600000024 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "MESH_darkbottom1"
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
                    constantValue: vec3 = { 0, 50, -40 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/aurora_base_emote_portal_mesh_topring.aurora_ass.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.501960814, 0.909803927, 1, 0.5 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.992156863, 0.996078432, 1, 0.729411781 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.140000001
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.992156863, 1, 1, 0.729411781 }
                            { 0.474509805, 0.478431374, 0.478431374, 0.729411781 }
                            { 0.356862754, 0.360784322, 0.360784322, 0.729411781 }
                            { 0.992156863, 1, 1, 0.729411781 }
                            { 0.992156863, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.699999988, 0.5, 0.699999988 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/zoe_base_z_color-hold006.aurora_ass.tex"
            }
        }
        particleName: string = "ass"
        particlePath: string = "Characters/ass"
    }


# VFX_HUB_NAME: tt
# VFX_HUB_DESCRIPTION: tt
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 5
    "tt" =     "Characters/Aurora/Skins/Skin0/Particles/Aurora_Base_Emote_SpiritPoof" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0199999996
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
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
                            0.800000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.119999997
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 275, 225 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 200
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 6
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 300
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "spark_shoot_up2"
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
                        constantValue: vec3 = { 10, 1, 0 }
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
                                { 10, 1, 0 }
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
                    constantValue: vec3 = { 0, 15, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.603921592, 0.988235295, 1, 0.501960814 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.603921592, 0.925490201, 1, 0.501960814 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.356862754, 0.670588255, 0.741176486, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 25
                }
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                directionVelocityScale: f32 = 0.00499999989
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 18, 18, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 18, 18, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            0.699999988
                            0.709999979
                            0.899999976
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 5 }
                            { 2, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 1, 1 }
                            { 0.300000012, 0.600000024, 1 }
                            { 0.5, 0.200000003, 1 }
                            { 0.5, 0.200000003, 1 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/base_generic_sparks_add.aurora_tt.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "BaseMist_outer2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 50, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 5 }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 2
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
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.449999988 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.831372559, 0.831372559, 0.831372559, 1 }
                            { 1, 1, 1, 0.501960814 }
                            { 0.533333361, 0.913725495, 1, 0.200000003 }
                            { 0.294117659, 0.870588243, 1, 0 }
                        }
                    }
                }
                pass: i16 = 9
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0.800000012
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                0.800000012
                                0.639999986
                                0.200000003
                                0
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/vfxhub/generic_erosion04.aurora_tt.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 90 }
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
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 360, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 5, 0 }
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
                            { 80, 5, 0 }
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
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1.20000005, 1.20000005, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/bunnymage_darkdust.aurora_tt.tex"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/vfxhub/aurora_cagradient.aurora_tt.tex"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    paletteCount: i32 = 4
                }
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/generic_holystrings_support.aurora_tt.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "BaseMist_outer3"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
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
                            { 50, 50, 50 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 5 }
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
                    constantValue: vec4 = { 0.498039216, 0.909803927, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.5
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.831372559, 0.831372559, 0.831372559, 1 }
                            { 0.992156863, 1, 1, 0.501960814 }
                            { 0.992156863, 1, 1, 0.200000003 }
                            { 0.498039216, 0.909803927, 1, 0 }
                        }
                    }
                }
                pass: i16 = 8
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0.800000012
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                0.800000012
                                0.639999986
                                0.200000003
                                0
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/vfxhub/generic_erosion04.aurora_tt.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 90 }
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
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 360, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 5, 0 }
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
                            { 50, 5, 0 }
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
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1.20000005, 1.20000005, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/generic_2x2_cloudpuff.aurora_tt.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/generic_holystrings_support.aurora_tt.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "BaseMist_outer4"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 50, 50 }
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
                            { 50, 50, 50 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 5 }
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
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.5 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.615686297, 0.870588243, 0.929411769, 0 }
                            { 0.121568628, 0.752941191, 0.894117653, 1 }
                            { 0.152941182, 0.650980413, 0.760784328, 0.250980407 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 7
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0.5
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.200000003
                                1
                            }
                            values: list[f32] = {
                                0
                                0.5
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/vfxhub/generic_mask04.aurora_tt.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 90 }
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
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 360, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 5, 0 }
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
                            { 50, 5, 0 }
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
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1.20000005, 1.20000005, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/generic_2x2_cloudpuff.aurora_tt.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/generic_holystrings_support.aurora_tt.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 7
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
                                    0.300000012
                                    0.550000012
                                    1
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
                    5
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    2
                }
                emitterName: string = "FireCards_CAST"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
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
                            { 100, 100, 100 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
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
                                { 15, 0, 0 }
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
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.501960814, 0.909803927, 1, 0.300000012 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.200000003
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.500007629 }
                            { 0.423529416, 0.894117653, 1, 0.368627459 }
                            { 0.0509803928, 0.368627459, 0.43921569, 0 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.200000003
                                0.485920578
                                1
                            }
                            values: list[f32] = {
                                0.361111104
                                0.797666013
                                1.25
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/aurora_base_wall_erosion.aurora_tt.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                depthBiasFactors: vec2 = { -1, -20 }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
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
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.223826721
                            0.476534307
                            1
                        }
                        values: list[vec3] = {
                            { 3, 0, 0 }
                            { 1.5, 0, 0 }
                            { 0.349206358, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 10, 0 }
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
                            { 50, 10, 0 }
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
                            { 0.349999994, 0, 0 }
                            { 0.714285731, 0, 0 }
                            { 1, 0, 0 }
                            { 0.75, 0, 0 }
                            { 0.649999976, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/aurora_base_fireshapes_00.aurora_tt.tex"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/vfxhub/aurora_cagradient2.aurora_tt.tex"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 4, 0, 0 }
                    }
                }
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "tt"
        particlePath: string = "Characters/tt"
        soundOnCreateDefault: string = "Play_sfx_Aurora_AuroraSpirits_buffdeactivate"
        flags: u16 = 198
    }


# VFX_HUB_NAME: ss
# VFX_HUB_DESCRIPTION: ss
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 6
    "Aurora_Base_BA_tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                        


# VFX_HUB_NAME: test2
# VFX_HUB_DESCRIPTION: test2
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 25
    "Aurora_Base_R_AoERingExpand" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                       


# VFX_HUB_NAME: test
# VFX_HUB_DESCRIPTION: test
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 6
    "Aurora_Base_BA_tar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}


# VFX_HUB_NAME: auroraexplison
# VFX_HUB_DESCRIPTION: auroraexplison
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 15
    "Aurora_Base_R_AoERingRecast" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }

     # VFX systems will be added below
 }