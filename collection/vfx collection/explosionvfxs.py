entries: map[hash,embed] = {

# VFX_HUB_NAME: testexplosionvfx
# VFX_HUB_DESCRIPTION: testexplosionvfx
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 3
    "testexplosionvfx" = VfxSystemDefinitionData {
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
        particleName: string = "testexplosionvfx"
        particlePath: string = "testexplosionvfx"
    }

# VFX_HUB_NAME: rtar
# VFX_HUB_DESCRIPTION: rtar
# VFX_HUB_CATEGORY: explosions
# VFX_HUB_EMITTERS: 24
    "rtar" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.150000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.270000011
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
                            0.270000011
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.6499996
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "FireLine"
                SpawnShape: pointer = VfxShapeCylinder {}
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                primitive: pointer = VfxPrimitiveRay {}
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
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.107407406
                            0.296296299
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.949019611, 1, 1 }
                            { 0, 0.894864619, 0.998194814, 1 }
                            { 0, 0.831372559, 0.996078432, 0.525581419 }
                            { 0, 0.568627477, 1, 0.301960796 }
                            { 0, 0.0156862754, 1, 0 }
                        }
                    }
                }
                pass: i16 = 8000
                miscRenderFlags: u8 = 1
                TextureFlipV: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 360, 180 }
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
                            { 180, 360, 180 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 1600, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 1600, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.314814836
                            0.6703704
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.731075704, 0 }
                            { 0.617529929, 0.955378473, 0 }
                            { 0.155378491, 0.978533387, 0 }
                            { 0, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_LighRay.SKINS_Jinx_Skin60_rtar.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "shockwaves"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 150, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Shockwave.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.160006106, 0.269993126, 0.540001512, 0.300007641 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0611111112
                            0.125
                            0.401851863
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.570000768 }
                            { 0, 0.330006868, 0.500007629, 0.251629442 }
                            { 0, 0, 0.499355465, 0.116279073 }
                            { 0, 0, 0.498039007, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.179629624
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                0.138844624
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.150000006
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Skin60_Q_Erode.SKINS_Jinx_Skin60_rtar.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 0, 5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 5 }
                            { 0, 0, 0.5 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3.79999995, 3.79999995, 15 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.39999998, 1.39999998, 0.200000003 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_Q_Trail_Smoke.SKINS_Jinx_Skin60_rtar.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.75, 0 }
                }
                texDiv: vec2 = { 0.5, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "shockwaves_out"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Shockwave.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.827450991, 0.827450991, 0.827450991, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.101851851
                            0.207407415
                            0.462962955
                            0.724074125
                            1
                        }
                        values: list[vec4] = {
                            { 0.256347567, 0.765797794, 0.824206114, 0 }
                            { 0, 0.0292041544, 0.0973471776, 0 }
                            { 0.0227143411, 0.175224915, 0.34071511, 1 }
                            { 0.0227143411, 0.175224915, 0.34071511, 0.788052917 }
                            { 0.0227143411, 0.175224915, 0.34071511, 0.487460107 }
                            { 0.0227143411, 0.175224915, 0.34071511, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.13333334
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                0.181872517
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.150000006
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Skin60_Q_Erode.SKINS_Jinx_Skin60_rtar.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
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
                            { -90, 0, 0 }
                        }
                    }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 0, 5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 5 }
                            { 0, 0, 0.5 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 4, 15 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 1 }
                            { 1, 1, 1.10000002 }
                            { 1.39999998, 1.39999998, 3 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_Q_Trail_Smoke.SKINS_Jinx_Skin60_rtar.dds"
                texDiv: vec2 = { 0.5, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 2, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec2] = {
                            { 4, 0 }
                            { 0.300000012, 0 }
                            { 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.219999999
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
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
                                    0.5
                                    2
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
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "fast_ground"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1400, 1200, 0 }
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
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1400, 1200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 4, 4 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -800, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -800, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 250
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
                    constantValue: vec4 = { 1, 1, 1, 0.850003839 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.850003839 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.678431392, 0.968627453, 1 }
                            { 0.192156866, 0.270588249, 0.290196091, 1 }
                            { 0.290196091, 0.270588249, 0.192156866, 1 }
                            { 0.109803922, 0.0941176489, 0.0705882385, 1 }
                        }
                    }
                }
                pass: i16 = 10
                depthBiasFactors: vec2 = { -1, -30 }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 150, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            { 50, 150, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.992592573
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_R_Rocks_2x2.SKINS_Jinx_Skin60_rtar.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.170000002
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.25
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
                emitterName: string = "Ground_Debris"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 1000, 0 }
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
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 500, 1000, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -600, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -600, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 350
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
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.800000012 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.129999995
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.678431392, 0.968627453, 1 }
                            { 0, 0.443137258, 0.635294139, 1 }
                            { 0.290196091, 0.270588249, 0.192156866, 1 }
                            { 0.109803922, 0.0941176489, 0.0705882385, 1 }
                        }
                    }
                }
                pass: i16 = 10
                depthBiasFactors: vec2 = { -1, -30 }
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 150, 1 }
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
                            { 40, 150, 1 }
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
                            { 1, 1, 1 }
                            { 0, 0, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_R_Rocks_2x2.SKINS_Jinx_Skin60_rtar.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Ring_AOE"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_R_Border_ring.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.996078432, 0.996078432, 0.996078432, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.14629668
                            0.427769989
                            0.643518507
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.996078432, 0.996078432, 0.996078432, 0 }
                            { 0, 0.828112245, 0.992172241, 1 }
                            { 0, 0.828112245, 0.992172241, 1 }
                            { 0.382806599, 0.996078432, 0, 1 }
                            { 0.132810459, 0.996078432, 0, 1 }
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
                                0.235059768
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Rework_Generic_NoiseMulti01.SKINS_Jinx_Skin60_rtar.dds"
                }
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 22, 22, 22 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
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
                            { 22, 22, 22 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.970000029
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.230753571
                            0.587037027
                            1
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0.40183267, 0.40183267 }
                            { 0.838495731, 0.834462106, 0.834462106 }
                            { 0.967808783, 0.967808783, 0.967808783 }
                            { 1.00999999, 1.00999999, 1.00999999 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_W_Border_lines.SKINS_Jinx_Skin60_rtar.dds"
                frameRate: f32 = 10
                numFrames: u16 = 4
                texDiv: vec2 = { 1, 4 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0 }
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
                            { 0.200000003, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
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
                                    0.600000024
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
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Ring_AOE1"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_R_Border_ring.SKINS_Jinx_Skin60_rtar.scb"
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
                    constantValue: vec4 = { 0.929411769, 0.482352942, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.14629668
                            0.525908351
                            0.735111654
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.929411769, 0.482352942, 1, 0 }
                            { 0.929411769, 0.482352942, 1, 1 }
                            { 0.929411769, 0.482352942, 1, 1 }
                            { 0.868282437, 0.269459277, 1, 0.367441863 }
                            { 0.790911198, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 4
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                1
                                0.408771306
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Rework_Generic_NoiseMulti01.SKINS_Jinx_Skin60_rtar.dds"
                }
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 23, 23, 23 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 23, 23, 23 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.262235045
                            0.58518517
                            1
                        }
                        values: list[vec3] = {
                            { 0.449999988, 0.449999988, 0.449999988 }
                            { 0.861125231, 0.857091606, 0.857091606 }
                            { 0.967808783, 0.967057645, 0.967057645 }
                            { 1.00999999, 1.00999999, 1.00999999 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_W_Border_lines.SKINS_Jinx_Skin60_rtar.dds"
                frameRate: f32 = 10
                numFrames: u16 = 4
                texDiv: vec2 = { 1, 4 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0 }
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
                            { 0.200000003, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.170000002
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
                                    0.5
                                    2
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
                    10.5500002
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "SpikeShapes"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1660, 500, 0 }
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
                            { 1660, 500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -10, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 300, 0, 0 }
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
                        { 0, 1, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.500007629, 0.439993888, 0.37000075, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.500007629, 0.439993888, 0.37000075, 0.600000024 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.177777782
                            0.542592645
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.701960802, 1, 0 }
                            { 0.545098066, 0.854901969, 1, 1 }
                            { 1, 1, 1, 0.465116262 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 20
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 40
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Skin60_E_ErosionShapes01.SKINS_Jinx_Skin60_rtar.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 1 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 200, 1 }
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
                            { 0.800000012, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_AnimeShapes02.SKINS_Jinx_Skin60_rtar.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.850000024
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
                            0.850000024
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "Wave_a"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_FlatDisc.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.600000024 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.103703715
                            0.375925928
                            0.790740728
                            1
                        }
                        values: list[vec4] = {
                            { 0.309803933, 0.925490201, 0.996078432, 0 }
                            { 0.58431375, 0, 1, 1 }
                            { 0.58431375, 0, 1, 0.666666687 }
                            { 0.400000006, 0, 1, 0.34117648 }
                            { 0.58431375, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0.297915906
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Skin60_PlasmaNoise.SKINS_Jinx_Skin60_rtar.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 1, 1 }
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
                            { 4, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_Shockwave.SKINS_Jinx_Skin60_rtar.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.499676794
                            1
                        }
                        values: list[vec2] = {
                            { 2, 0.75 }
                            { 2, 2.49493527 }
                            { 2, 2.75 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Jinx_Skin60_LightningFlash_Mult.SKINS_Jinx_Skin60_rtar.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.109999999
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.850000024
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
                            0.850000024
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "Wave_a1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_FlatDisc.SKINS_Jinx_Skin60_rtar.scb"
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
                            0.103703715
                            0.381481498
                            0.740740716
                            1
                        }
                        values: list[vec4] = {
                            { 0.309803933, 0.925490201, 0.996078432, 0 }
                            { 0, 0.168627456, 0.43921569, 1 }
                            { 0, 0.168627456, 0.43921569, 0.677701771 }
                            { 0, 0, 0.43921569, 0.270588249 }
                            { 0, 0.0235294122, 0.43921569, 0 }
                        }
                    }
                }
                pass: i16 = 102
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0.297915906
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Skin60_PlasmaNoise.SKINS_Jinx_Skin60_rtar.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4, 1, 1 }
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
                            { 4, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_Shockwave.SKINS_Jinx_Skin60_rtar.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.499676794
                            1
                        }
                        values: list[vec2] = {
                            { 2, 0.75 }
                            { 2, 2.49493527 }
                            { 2, 2.75 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Jinx_Skin60_LightningFlash_Mult.SKINS_Jinx_Skin60_rtar.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.150000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                lifetime: option[f32] = {
                    1.14999998
                }
                isSingleParticle: flag = true
                emitterName: string = "poolSphere_small"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -50, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_Particles_1_1581.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0941176489, 0.0470588244, 0.235294119, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.00370370364
                            0.100000001
                            0.485644728
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 45
                depthBiasFactors: vec2 = { -1, -50 }
                isUniformScale: flag = true
                uvScrollClamp: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 4.19999981, 3, 3 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.204742342
                            1
                        }
                        values: list[vec3] = {
                            { 0.27888447, 0.254980087, 0.254980087 }
                            { 0.68527782, 0.673325598, 0.673325598 }
                            { 0.78798753, 0.78798753, 0.78798753 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_Particles_1_291.SKINS_Jinx_Skin60_rtar.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.800000012 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.100000001 }
                }
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.140000001
                }
                lifetime: option[f32] = {
                    0.910000026
                }
                isSingleParticle: flag = true
                emitterName: string = "IMPACT_dot"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.68235296, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.368518502
                            0.91814816
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.68235296, 1, 1 }
                            { 0, 0.68235296, 1, 1 }
                            { 0, 0.68235296, 1, 1 }
                            { 0, 0.68235296, 1, 1 }
                        }
                    }
                }
                pass: i16 = 9000
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    1
                                }
                                keyValues: list[f32] = {
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
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
                    constantValue: vec3 = { 250, 400, 400 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.359259218
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.0500000007, 0.0500000007 }
                            { 0.488645405, 0.0500000007, 0.0500000007 }
                            { 0.171115547, 0.0500000007, 0.0500000007 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_Impact_dot.SKINS_Jinx_Skin60_rtar.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.0799999982
                }
                particleLinger: option[f32] = {
                    10.1000004
                }
                lifetime: option[f32] = {
                    0.150000006
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "Negative_Flash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.239215687, 0, 0.388235301, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.833333373
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0.31764707, 1, 0 }
                        }
                    }
                }
                pass: i16 = 9999
                depthBiasFactors: vec2 = { -1, -25 }
                miscRenderFlags: u8 = 1
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
                                    -360
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
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 250, 0 }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 250, 250, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.509259224
                            1
                        }
                        values: list[vec3] = {
                            { 0.646007955, 0.382470131, 0 }
                            { 0.935649395, 0.856573701, 1 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_BA_Hit_Impact.SKINS_Jinx_Skin60_rtar.dds"
                numFrames: u16 = 2
                texDiv: vec2 = { 2, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
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
                                    0.300000012
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
                    0.100000001
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Negative_Sparkz"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 20, 0 }
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
                            { 50, 20, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 20
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_Finisher_shot02_003.SKINS_Jinx_Skin60_rtar.scb"
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
                            0.410493821
                            0.422839493
                            0.734567881
                            1
                        }
                        values: list[vec4] = {
                            { 0.239215687, 0, 0.388235301, 1 }
                            { 0.239215687, 0, 0.388235301, 1 }
                            { 0, 0.996078432, 0.498039216, 1 }
                            { 0, 0.996078432, 0.529411793, 1 }
                            { 0, 0.996078432, 0, 1 }
                        }
                    }
                }
                pass: i16 = 150
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                0.37388888
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Skin60_Finisher_Outro_ScreenLight01.SKINS_Jinx_Skin60_rtar.tex"
                }
                disableBackfaceCull: bool = true
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 23, 80 }
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
                            { 0, 23, 80 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.75, 0.5, 0.5 }
                            { 1.20000005, 0.800000012, 0.800000012 }
                            { 1.5, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Aatrox_Skin33_Q_White.SKINS_Jinx_Skin60_rtar.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.300000012 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 10, 1 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Jinx_Skin60_Finisher_shot02_002.SKINS_Jinx_Skin60_rtar.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 10, 1.20000005 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, 0 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.109999999 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.150000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                }
                particleLinger: option[f32] = {
                    0.600000024
                }
                isSingleParticle: flag = true
                emitterName: string = "Ground_Ring_smoke1"
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_Q_01.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.262962997
                            0.701851845
                            1
                        }
                        values: list[vec4] = {
                            { 0.105882354, 0.227450982, 0.411764711, 0 }
                            { 0, 0.764705896, 1, 1 }
                            { 0, 0.764705896, 1, 0.569357038 }
                            { 0.0560553595, 0.488130867, 0.697180629, 0.34046945 }
                            { 0.105882354, 0.227450982, 0.411764711, 0 }
                        }
                    }
                }
                pass: i16 = 50
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 40
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.220370367
                                0.618518531
                                1
                            }
                            values: list[f32] = {
                                0
                                0.132799998
                                0.547200024
                                1.20000005
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Skin60_Q_Trail_Mult.SKINS_Jinx_Skin60_rtar.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 5, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.174074084
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.998007953, 0.998007953 }
                            { 1.09265721, 1.09265721, 1.09265721 }
                            { 1.35258961, 1.35258961, 1.35258961 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_Q_15.SKINS_Jinx_Skin60_rtar.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.400000006 }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec2] = {
                            { 0, -4 }
                            { 0, -1 }
                            { 0, -0.5 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 3, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.150000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.449999988
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
                            0.449999988
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.100000001
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Negative_Sparkz1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 20, 0 }
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
                            { 50, 20, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 50
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_Finisher_shot02_003.SKINS_Jinx_Skin60_rtar.scb"
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
                            0.217592597
                            0.22839506
                            0.734567881
                            1
                        }
                        values: list[vec4] = {
                            { 0.384313732, 0.145098045, 0.678431392, 1 }
                            { 0.384313732, 0.145098045, 0.678431392, 1 }
                            { 0.90196079, 0.403921574, 1, 1 }
                            { 0.90196079, 0.403921574, 1, 1 }
                            { 0.890196085, 0.0588235296, 1, 1 }
                        }
                    }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                0.37388888
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Skin60_Finisher_Outro_ScreenLight01.SKINS_Jinx_Skin60_rtar.tex"
                }
                disableBackfaceCull: bool = true
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                directionVelocityScale: f32 = 0.00100000005
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 23, 80 }
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
                            { 0, 23, 80 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.75, 0.5, 0.5 }
                            { 1.20000005, 0.800000012, 0.800000012 }
                            { 1.5, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Aatrox_Skin33_Q_White.SKINS_Jinx_Skin60_rtar.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.300000012 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 10, 1 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Jinx_Skin60_Finisher_shot02_002.SKINS_Jinx_Skin60_rtar.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 10, 1.20000005 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, 0 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.109999999 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                                    0.600000024
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
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Ground_Ring"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_R_Border_ring.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.996078432, 0.996078432, 0.996078432, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.188885018
                            0.369661272
                            0.427769989
                            0.705449164
                            0.800910175
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0, 0.828112245, 0.992172241, 0 }
                            { 0, 0.828112245, 0.992172241, 1 }
                            { 0, 0.828112245, 0.992172241, 1 }
                            { 0, 0.996078432, 0.249996156, 1 }
                            { 0, 0.996078432, 0.414056122, 1 }
                            { 0, 0.347650915, 0.996078432, 1 }
                            { 0.363275677, 0, 0.996078432, 0 }
                        }
                    }
                }
                pass: i16 = 44
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.198148131
                                0.518518507
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                0.100000001
                                0.558964133
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Rework_Generic_NoiseMulti01.SKINS_Jinx_Skin60_rtar.dds"
                }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1.14999998
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.970000029
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.252975792
                            0.603703678
                            1
                        }
                        values: list[vec3] = {
                            { 0.890495062, 0.889459193, 0.889459193 }
                            { 0.936635077, 0.932601452, 0.932601452 }
                            { 0.980031908, 0.980031908, 0.980031908 }
                            { 1.00999999, 1.00999999, 1.00999999 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_W_Border_lines.SKINS_Jinx_Skin60_rtar.dds"
                frameRate: f32 = 10
                numFrames: u16 = 4
                texDiv: vec2 = { 1, 4 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0 }
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
                            { 0.200000003, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
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
                                    0.600000024
                                    1
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
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Ground_Ring1"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_R_Border_ring.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.929411769, 0.482352942, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.188885018
                            0.427769989
                            0.800910175
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.929411769, 0.482352942, 1, 0 }
                            { 0.929411769, 0.482352942, 1, 1 }
                            { 0.929411769, 0.482352942, 1, 1 }
                            { 0.495686263, 0, 1, 1 }
                            { 0.419146478, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 43
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.268518507
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Rework_Generic_NoiseMulti01.SKINS_Jinx_Skin60_rtar.dds"
                }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 16, 0, 16 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 16, 0, 16 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.970000029
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.252975792
                            0.603703678
                            1
                        }
                        values: list[vec3] = {
                            { 0.890495062, 0.889459193, 0.889459193 }
                            { 0.936635077, 0.932601452, 0.932601452 }
                            { 0.980031908, 0.980031908, 0.980031908 }
                            { 1.00999999, 1.00999999, 1.00999999 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_W_Border_lines.SKINS_Jinx_Skin60_rtar.dds"
                frameRate: f32 = 10
                numFrames: u16 = 4
                texDiv: vec2 = { 1, 4 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0 }
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
                            { 0.200000003, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.600000024
                }
                lifetime: option[f32] = {
                    0.699999988
                }
                emitterName: string = "Ground_Ring_smoke2"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_Q_01.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.0470588244, 0.270588249, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 0.0470588244, 0.270588249, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0907407403
                            0.368518561
                            0.688888907
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 55
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 40
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.21851851
                                0.598148167
                                1
                            }
                            values: list[f32] = {
                                0.449999988
                                0.618375659
                                0.934927225
                                1.20000005
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Skin60_Q_Trail_Mult.SKINS_Jinx_Skin60_rtar.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isUniformScale: flag = true
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
                                    360
                                    -360
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
                    constantValue: vec3 = { 60, 5, 50 }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_UX_Psychosis_Lines_1.SKINS_Jinx_Skin60_rtar.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.99000001, 0 }
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
                            { 0.99000001, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 5, 2 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.170000002
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
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
                            0.75
                        }
                    }
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Dome_Smears"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_R_Dome.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.996078432, 0.996078432, 0.996078432, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.188885018
                            0.369661272
                            0.427769989
                            0.590574384
                            0.800910175
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0, 0.828112245, 0.992172241, 0 }
                            { 0, 0.828112245, 0.992172241, 1 }
                            { 0, 0.828112245, 0.992172241, 1 }
                            { 0, 0.996078432, 0.249996156, 1 }
                            { 0, 0.996078432, 0.414056122, 1 }
                            { 0, 0.347650915, 0.996078432, 1 }
                            { 0.363275677, 0, 0.996078432, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.198148131
                                0.518518507
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                0.100000001
                                0.558964133
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Rework_Generic_NoiseMulti01.SKINS_Jinx_Skin60_rtar.dds"
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 10 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 25, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1.14999998
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.850000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 25, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.970000029
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.262235045
                            0.612962961
                            1
                        }
                        values: list[vec3] = {
                            { 0.492350608, 0.492350608, 0.492350608 }
                            { 0.851575315, 0.84754169, 0.84754169 }
                            { 0.936286867, 0.936286867, 0.936286867 }
                            { 1.00999999, 1.00999999, 1.00999999 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_W_Border_lines.SKINS_Jinx_Skin60_rtar.dds"
                frameRate: f32 = 10
                numFrames: u16 = 4
                texDiv: vec2 = { 1, 4 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0 }
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
                            { 0.200000003, 0 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Jinx_Skin60_W_BorderTop_mask.SKINS_Jinx_Skin60_rtar.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.170000002
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
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
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Dome_Smears1"
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_R_Dome.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.996078432, 0.996078432, 0.996078432, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.188885018
                            0.472222209
                            0.547839522
                            0.814733326
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.925767004, 0.480461359, 0.996078432, 0 }
                            { 0.996078432, 0.39061898, 0.843737006, 1 }
                            { 0.996078432, 0.39061898, 0.843737006, 1 }
                            { 0.996078432, 0.0390619002, 0.246089965, 1 }
                            { 0.996078432, 0.0598176233, 0.243783772, 0.841860473 }
                            { 0.996078432, 0.0742176101, 0.242183775, 0 }
                        }
                    }
                }
                pass: i16 = 99
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.198148131
                                0.518518507
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                0.100000001
                                0.558964133
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Rework_Generic_NoiseMulti01.SKINS_Jinx_Skin60_rtar.dds"
                }
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 10 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 25, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    1.14999998
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.850000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 25, 20 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.970000029
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.277049869
                            0.603703678
                            1
                        }
                        values: list[vec3] = {
                            { 0.482629478, 0.482629478, 0.482629478 }
                            { 0.841854215, 0.83782059, 0.83782059 }
                            { 0.928996027, 0.928996027, 0.928996027 }
                            { 1.00999999, 1.00999999, 1.00999999 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_W_Border_lines.SKINS_Jinx_Skin60_rtar.dds"
                frameRate: f32 = 10
                numFrames: u16 = 4
                texDiv: vec2 = { 1, 4 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0.200000003, 0 }
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
                            { 0.200000003, 0 }
                        }
                    }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Jinx_Skin60_W_BorderTop_mask.SKINS_Jinx_Skin60_rtar.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.144999996
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    0.910000026
                }
                isSingleParticle: flag = true
                emitterName: string = "Dome1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.68235296, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.33518517
                            0.58851856
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.68235296, 1, 1 }
                            { 0, 0.68235296, 1, 0.744186044 }
                            { 0, 0.68235296, 1, 0.432558119 }
                            { 0, 0.68235296, 1, 0 }
                        }
                    }
                }
                pass: i16 = 9000
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    1
                                }
                                keyValues: list[f32] = {
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    0
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
                    constantValue: vec3 = { 350, 400, 400 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.327777773
                            1
                        }
                        values: list[vec3] = {
                            { 0.277091622, 0.0500000007, 0.0500000007 }
                            { 0.61733067, 0.5, 0.5 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_Particles_1_1533.SKINS_Jinx_Skin60_rtar.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.600000024
                }
                lifetime: option[f32] = {
                    0.699999988
                }
                emitterName: string = "Ground_Ring_smoke3"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/vfxhub/Jinx_Skin60_Q_01.SKINS_Jinx_Skin60_rtar.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0500038154, 1, 0.429999232, 0.700007617 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.0500038154, 1, 0.429999232, 0.700007617 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0407407396
                            0.368518561
                            0.91481483
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 55
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 40
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.21851851
                                0.598148167
                                1
                            }
                            values: list[f32] = {
                                0.449999988
                                0.618375659
                                0.934927225
                                1.20000005
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/vfxhub/Jinx_Skin60_Q_Trail_Mult.SKINS_Jinx_Skin60_rtar.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isUniformScale: flag = true
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
                                    360
                                    -360
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
                    constantValue: vec3 = { 60, 5, 50 }
                }
                texture: string = "ASSETS/vfxhub/Jinx_Skin60_UX_Psychosis_Lines_1.SKINS_Jinx_Skin60_rtar.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.99000001, 0 }
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
                            { 0.99000001, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 5, 2 }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 90
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    1.10000002
                }
                emitterName: string = "BLADSjlaksd"
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00300000003
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.533333361, 0, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0777777806
                            0.274074078
                            0.696296275
                            1
                        }
                        values: list[vec4] = {
                            { 0.533333361, 0, 1, 0 }
                            { 0.533333361, 0, 1, 1 }
                            { 0.533333361, 0, 1, 1 }
                            { 0.533333361, 0, 1, 0.390697688 }
                            { 0.533333361, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = -90
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    360
                                    -360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 450, 0 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 1, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/vfxhub/Aura_Self.SKINS_Jinx_Skin60_rtar.DDS"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/vfxhub/Jinx_Skin60_UX_Psychosis_Lines_3.SKINS_Jinx_Skin60_rtar.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 2 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
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
                }
            }
        }
        particleName: string = "rtar"
        particlePath: string = "rtar"
        soundOnCreateDefault: string = "Play_sfx_Draven_DravenR_hit"
        flags: u16 = 198
        transform: mtx44 = {
            0.800000012, 0, 0, 0
            0, 0.800000012, 0, 0
            0, 0, 0.800000012, 0
            0, -150, 0, 1
        }
    }





     "Characters/Aurora/Skins/Skin0/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "testexplosionvfx" = "testexplosionvfx"
            
            "rtar" = "rtar"
        }
     }
} 
