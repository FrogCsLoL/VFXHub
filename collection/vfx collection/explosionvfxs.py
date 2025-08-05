entries: map[hash,embed] = {

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