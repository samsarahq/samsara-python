# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .vehicle_stats_aux_input_decoration import VehicleStatsAuxInputDecoration
from .vehicle_stats_decorations_ambient_air_temperature_milli_c import (
    VehicleStatsDecorationsAmbientAirTemperatureMilliC,
)
from .vehicle_stats_decorations_barometric_pressure_pa import VehicleStatsDecorationsBarometricPressurePa
from .vehicle_stats_decorations_battery_milli_volts import VehicleStatsDecorationsBatteryMilliVolts
from .vehicle_stats_decorations_def_level_milli_percent import VehicleStatsDecorationsDefLevelMilliPercent
from .vehicle_stats_decorations_ecu_speed_mph import VehicleStatsDecorationsEcuSpeedMph
from .vehicle_stats_decorations_engine_coolant_temperature_milli_c import (
    VehicleStatsDecorationsEngineCoolantTemperatureMilliC,
)
from .vehicle_stats_decorations_engine_load_percent import VehicleStatsDecorationsEngineLoadPercent
from .vehicle_stats_decorations_engine_oil_pressure_k_pa import VehicleStatsDecorationsEngineOilPressureKPa
from .vehicle_stats_decorations_engine_rpm import VehicleStatsDecorationsEngineRpm
from .vehicle_stats_decorations_engine_states import VehicleStatsDecorationsEngineStates
from .vehicle_stats_decorations_fuel_percents import VehicleStatsDecorationsFuelPercents
from .vehicle_stats_decorations_gps import VehicleStatsDecorationsGps
from .vehicle_stats_decorations_gps_distance_meters import VehicleStatsDecorationsGpsDistanceMeters
from .vehicle_stats_decorations_gps_odometer_meters import VehicleStatsDecorationsGpsOdometerMeters
from .vehicle_stats_decorations_intake_manifold_temperature_milli_c import (
    VehicleStatsDecorationsIntakeManifoldTemperatureMilliC,
)
from .vehicle_stats_decorations_obd_engine_seconds import VehicleStatsDecorationsObdEngineSeconds
from .vehicle_stats_decorations_obd_odometer_meters import VehicleStatsDecorationsObdOdometerMeters
from .vehicle_stats_engine_immobilizer import VehicleStatsEngineImmobilizer
from .vehicle_stats_ev_average_battery_temperature_milli_celsius import (
    VehicleStatsEvAverageBatteryTemperatureMilliCelsius,
)
from .vehicle_stats_ev_battery_current_milli_amp import VehicleStatsEvBatteryCurrentMilliAmp
from .vehicle_stats_ev_battery_state_of_health_milli_percent import VehicleStatsEvBatteryStateOfHealthMilliPercent
from .vehicle_stats_ev_battery_voltage_milli_volt import VehicleStatsEvBatteryVoltageMilliVolt
from .vehicle_stats_ev_charging_current_milli_amp import VehicleStatsEvChargingCurrentMilliAmp
from .vehicle_stats_ev_charging_energy_micro_wh import VehicleStatsEvChargingEnergyMicroWh
from .vehicle_stats_ev_charging_status import VehicleStatsEvChargingStatus
from .vehicle_stats_ev_charging_voltage_milli_volt import VehicleStatsEvChargingVoltageMilliVolt
from .vehicle_stats_ev_consumed_energy_micro_wh import VehicleStatsEvConsumedEnergyMicroWh
from .vehicle_stats_ev_distance_driven_meters import VehicleStatsEvDistanceDrivenMeters
from .vehicle_stats_ev_regenerated_energy_micro_wh import VehicleStatsEvRegeneratedEnergyMicroWh
from .vehicle_stats_ev_state_of_charge_milli_percent import VehicleStatsEvStateOfChargeMilliPercent
from .vehicle_stats_fault_codes_value import VehicleStatsFaultCodesValue
from .vehicle_stats_seatbelt_driver import VehicleStatsSeatbeltDriver
from .vehicle_stats_spreader_active import VehicleStatsSpreaderActive
from .vehicle_stats_spreader_air_temp import VehicleStatsSpreaderAirTemp
from .vehicle_stats_spreader_blast_state import VehicleStatsSpreaderBlastState
from .vehicle_stats_spreader_granular_name import VehicleStatsSpreaderGranularName
from .vehicle_stats_spreader_granular_rate import VehicleStatsSpreaderGranularRate
from .vehicle_stats_spreader_liquid_name import VehicleStatsSpreaderLiquidName
from .vehicle_stats_spreader_liquid_rate import VehicleStatsSpreaderLiquidRate
from .vehicle_stats_spreader_on_state import VehicleStatsSpreaderOnState
from .vehicle_stats_spreader_plow_status import VehicleStatsSpreaderPlowStatus
from .vehicle_stats_spreader_prewet_name import VehicleStatsSpreaderPrewetName
from .vehicle_stats_spreader_prewet_rate import VehicleStatsSpreaderPrewetRate
from .vehicle_stats_spreader_road_temp import VehicleStatsSpreaderRoadTemp
from .vehicle_stats_tire_pressures import VehicleStatsTirePressures


class VehicleStatsDecorations(UniversalBaseModel):
    """
    Optional decorations to the primary stat event. See [here](doc:decorations) for more details. The example shows the response if you were to submit `decorations=engineStates&obdEngineSeconds` to the query parameter:

    ```json
    "decorations":{
      "engineStates": {
        "value": "Off"
      },
      "obdEngineSeconds": {
        "value": 9723103
      }
    }
    ```
    """

    ambient_air_temperature_milli_c: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsAmbientAirTemperatureMilliC],
        FieldMetadata(alias="ambientAirTemperatureMilliC"),
    ] = None
    aux_input_1: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput1")
    ] = None
    aux_input_10: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput10")
    ] = None
    aux_input_11: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput11")
    ] = None
    aux_input_12: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput12")
    ] = None
    aux_input_13: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput13")
    ] = None
    aux_input_2: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput2")
    ] = None
    aux_input_3: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput3")
    ] = None
    aux_input_4: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput4")
    ] = None
    aux_input_5: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput5")
    ] = None
    aux_input_6: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput6")
    ] = None
    aux_input_7: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput7")
    ] = None
    aux_input_8: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput8")
    ] = None
    aux_input_9: typing_extensions.Annotated[
        typing.Optional[VehicleStatsAuxInputDecoration], FieldMetadata(alias="auxInput9")
    ] = None
    barometric_pressure_pa: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsBarometricPressurePa], FieldMetadata(alias="barometricPressurePa")
    ] = None
    battery_milli_volts: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsBatteryMilliVolts], FieldMetadata(alias="batteryMilliVolts")
    ] = None
    def_level_milli_percent: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsDefLevelMilliPercent], FieldMetadata(alias="defLevelMilliPercent")
    ] = None
    ecu_speed_mph: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsEcuSpeedMph], FieldMetadata(alias="ecuSpeedMph")
    ] = None
    engine_coolant_temperature_milli_c: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsEngineCoolantTemperatureMilliC],
        FieldMetadata(alias="engineCoolantTemperatureMilliC"),
    ] = None
    engine_immobilizer: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEngineImmobilizer], FieldMetadata(alias="engineImmobilizer")
    ] = None
    engine_load_percent: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsEngineLoadPercent], FieldMetadata(alias="engineLoadPercent")
    ] = None
    engine_oil_pressure_k_pa: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsEngineOilPressureKPa], FieldMetadata(alias="engineOilPressureKPa")
    ] = None
    engine_rpm: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsEngineRpm], FieldMetadata(alias="engineRpm")
    ] = None
    engine_states: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsEngineStates], FieldMetadata(alias="engineStates")
    ] = None
    ev_average_battery_temperature_milli_celsius: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvAverageBatteryTemperatureMilliCelsius],
        FieldMetadata(alias="evAverageBatteryTemperatureMilliCelsius"),
    ] = None
    ev_battery_current_milli_amp: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvBatteryCurrentMilliAmp], FieldMetadata(alias="evBatteryCurrentMilliAmp")
    ] = None
    ev_battery_state_of_health_milli_percent: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvBatteryStateOfHealthMilliPercent],
        FieldMetadata(alias="evBatteryStateOfHealthMilliPercent"),
    ] = None
    ev_battery_voltage_milli_volt: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvBatteryVoltageMilliVolt], FieldMetadata(alias="evBatteryVoltageMilliVolt")
    ] = None
    ev_charging_current_milli_amp: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvChargingCurrentMilliAmp], FieldMetadata(alias="evChargingCurrentMilliAmp")
    ] = None
    ev_charging_energy_micro_wh: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvChargingEnergyMicroWh], FieldMetadata(alias="evChargingEnergyMicroWh")
    ] = None
    ev_charging_status: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvChargingStatus], FieldMetadata(alias="evChargingStatus")
    ] = None
    ev_charging_voltage_milli_volt: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvChargingVoltageMilliVolt], FieldMetadata(alias="evChargingVoltageMilliVolt")
    ] = None
    ev_consumed_energy_micro_wh: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvConsumedEnergyMicroWh], FieldMetadata(alias="evConsumedEnergyMicroWh")
    ] = None
    ev_distance_driven_meters: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvDistanceDrivenMeters], FieldMetadata(alias="evDistanceDrivenMeters")
    ] = None
    ev_regenerated_energy_micro_wh: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvRegeneratedEnergyMicroWh], FieldMetadata(alias="evRegeneratedEnergyMicroWh")
    ] = None
    ev_state_of_charge_milli_percent: typing_extensions.Annotated[
        typing.Optional[VehicleStatsEvStateOfChargeMilliPercent], FieldMetadata(alias="evStateOfChargeMilliPercent")
    ] = None
    fault_codes: typing_extensions.Annotated[
        typing.Optional[VehicleStatsFaultCodesValue], FieldMetadata(alias="faultCodes")
    ] = None
    fuel_percents: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsFuelPercents], FieldMetadata(alias="fuelPercents")
    ] = None
    gps: typing.Optional[VehicleStatsDecorationsGps] = None
    gps_distance_meters: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsGpsDistanceMeters], FieldMetadata(alias="gpsDistanceMeters")
    ] = None
    gps_odometer_meters: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsGpsOdometerMeters], FieldMetadata(alias="gpsOdometerMeters")
    ] = None
    intake_manifold_temperature_milli_c: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsIntakeManifoldTemperatureMilliC],
        FieldMetadata(alias="intakeManifoldTemperatureMilliC"),
    ] = None
    obd_engine_seconds: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsObdEngineSeconds], FieldMetadata(alias="obdEngineSeconds")
    ] = None
    obd_odometer_meters: typing_extensions.Annotated[
        typing.Optional[VehicleStatsDecorationsObdOdometerMeters], FieldMetadata(alias="obdOdometerMeters")
    ] = None
    seatbelt_driver: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSeatbeltDriver], FieldMetadata(alias="seatbeltDriver")
    ] = None
    spreader_active: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderActive], FieldMetadata(alias="spreaderActive")
    ] = None
    spreader_air_temp: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderAirTemp], FieldMetadata(alias="spreaderAirTemp")
    ] = None
    spreader_blast_state: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderBlastState], FieldMetadata(alias="spreaderBlastState")
    ] = None
    spreader_granular_name: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderGranularName], FieldMetadata(alias="spreaderGranularName")
    ] = None
    spreader_granular_rate: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderGranularRate], FieldMetadata(alias="spreaderGranularRate")
    ] = None
    spreader_liquid_name: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderLiquidName], FieldMetadata(alias="spreaderLiquidName")
    ] = None
    spreader_liquid_rate: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderLiquidRate], FieldMetadata(alias="spreaderLiquidRate")
    ] = None
    spreader_on_state: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderOnState], FieldMetadata(alias="spreaderOnState")
    ] = None
    spreader_plow_status: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderPlowStatus], FieldMetadata(alias="spreaderPlowStatus")
    ] = None
    spreader_prewet_name: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderPrewetName], FieldMetadata(alias="spreaderPrewetName")
    ] = None
    spreader_prewet_rate: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderPrewetRate], FieldMetadata(alias="spreaderPrewetRate")
    ] = None
    spreader_road_temp: typing_extensions.Annotated[
        typing.Optional[VehicleStatsSpreaderRoadTemp], FieldMetadata(alias="spreaderRoadTemp")
    ] = None
    tire_pressure: typing_extensions.Annotated[
        typing.Optional[VehicleStatsTirePressures], FieldMetadata(alias="tirePressure")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
