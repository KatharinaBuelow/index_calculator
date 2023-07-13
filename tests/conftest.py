import pandas as pd
import pooch
import xarray as xr

url_base = "https://github.com/ludwiglierhammer/test_data/raw/main/"


def _pooch_retrieve(url, known_hash=None):
    return pooch.retrieve(url, known_hash=known_hash)


def tas_day_netcdf():
    url = (
        url_base
        + "/tas/day/tas_EUR-11_MPI-M-MPI-ESM-LR_historical_r3i1p1_GERICS-REMO2015_v1_day_20010101-20010107.nc"  # noqa
    )
    return _pooch_retrieve(url)


def pr_day_netcdf():
    url = (
        url_base
        + "/pr/day/pr_EUR-11_MPI-M-MPI-ESM-LR_historical_r3i1p1_GERICS-REMO2015_v1_day_20010101-20010107.nc"  # noqa
    )
    return _pooch_retrieve(url)


def tas_series(values, **kwargs):
    def _tas_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="tas",
            attrs={
                "standard_name": "air_temperature",
                "cell_methods": "time: mean within days",
                "units": "K",
            },
        )

    return _tas_series(values, **kwargs)


def pr_series(values, **kwargs):
    def _pr_series(values, start="1/1/2000", units="kg m-2 s-1", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="pr",
            attrs={
                "standard_name": "precipitation_flux",
                "cell_methods": "time: mean within days",
                "units": units,
            },
        )

    return _pr_series(values, **kwargs)


def tasmin_series(values, **kwargs):
    def _tasmin_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="tasmin",
            attrs={
                "standard_name": "air_temperature",
                "cell_methods": "time: minimum within days",
                "units": "K",
            },
        )

    return _tasmin_series(values, **kwargs)


def tasmax_series(values, **kwargs):
    def _tasmax_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="tasmax",
            attrs={
                "standard_name": "air_temperature",
                "cell_methods": "time: maximum within days",
                "units": "K",
            },
        )

    return _tasmax_series(values, **kwargs)


def prsn_series(values, **kwargs):
    def _prsn_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="prsn",
            attrs={
                "standard_name": "snowfall_flux",
                "cell_methods": "time: mean",
                "units": "kg m-2 s-1",
            },
        )

    return _prsn_series(values, **kwargs)


def snd_series(values, **kwargs):
    def _snd_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="snd",
            attrs={
                "standard_name": "surface_snow_thickness",
                "cell_methods": "time: mean",
                "units": "m",
            },
        )

    return _snd_series(values, **kwargs)


def hurs_series(values, **kwargs):
    def _hurs_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="hurs",
            attrs={
                "standard_name": "relative_humidity",
                "cell_methods": "time: mean",
                "units": "%",
            },
        )

    return _hurs_series(values, **kwargs)


def rsds_series(values, **kwargs):
    def _rsds_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="rsds",
            attrs={
                "standard_name": "surface_downwelling_shortwave_flux",
                "cell_methods": "time: mean",
                "units": "W m-2",
            },
        )

    return _rsds_series(values, **kwargs)


def rsus_series(values, **kwargs):
    def _rsus_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="rsus",
            attrs={
                "standard_name": "surface_upwelling_shortwave_flux",
                "cell_methods": "time: mean",
                "units": "W m-2",
            },
        )

    return _rsus_series(values, **kwargs)


def rlds_series(values, **kwargs):
    def _rlds_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="rlds",
            attrs={
                "standard_name": "surface_downwelling_longwave_flux",
                "cell_methods": "time: mean",
                "units": "W m-2",
            },
        )

    return _rlds_series(values, **kwargs)


def rlus_series(values, **kwargs):
    def _rlus_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="rlus",
            attrs={
                "standard_name": "surface_upwelling_longwave_flux",
                "cell_methods": "time: mean",
                "units": "W m-2",
            },
        )

    return _rlus_series(values, **kwargs)


def sfcWind_series(values, **kwargs):
    def _sfcWind_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="sfcWind",
            attrs={
                "standard_name": "wind_speed",
                "cell_methods": "time: mean",
                "units": "m s-1",
            },
        )

    return _sfcWind_series(values, **kwargs)


def mrt_series(values, **kwargs):
    def _mrt_series(values, start="1/1/2000", freq="D"):
        coords = pd.date_range(start, periods=len(values), freq=freq)
        return xr.DataArray(
            values,
            coords=[coords],
            dims="time",
            name="mrt",
            attrs={
                "standard_name": "mean_radiant_temperature",
                "cell_methods": "time: mean",
                "units": "K",
            },
        )

    return _mrt_series(values, **kwargs)
