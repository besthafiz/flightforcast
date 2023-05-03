# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Join orgin flight and country

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import datetime
import statsmodels.tsa.api as smt
from IPython.display import display
from pandasql import *
from dateutil import parser
import pandasql as ps


# %%
def parseDepartureDate(orgn_dst_flight_contry_df):
    print("--")
    orgn_dst_flight_contry_df['SCH_DEP_DATE'] = pd.to_datetime(orgn_dst_flight_contry_df['SCH_DEP_DATE']).dt.date


# %%
def renameOrgDstFltCntryDfColumns(orgn_dst_flight_contry_df):
    orgn_dst_flight_contry_df['ORG_CNTRY_NAME'] = orgn_dst_flight_contry_df['ORG_CNTRY_NAME'].str.upper()
    orgn_dst_flight_contry_df['DST_CNTRY_NAME'] = orgn_dst_flight_contry_df['DST_CNTRY_NAME'].str.upper()
    orgn_dst_flight_contry_df['ORG_CNTRY_NAME'] = orgn_dst_flight_contry_df['ORG_CNTRY_NAME'].str.strip()
    orgn_dst_flight_contry_df['DST_CNTRY_NAME'] = orgn_dst_flight_contry_df['DST_CNTRY_NAME'].str.strip()


# %%
def getSelectedHolidayCol(selected_holiday_col_df):
    selected_holiday_col_df=selected_holiday_col_df[['Country',	'From_date','to_date']]
    selected_holiday_col_df['Country'] = selected_holiday_col_df['Country'].str.upper()
    selected_holiday_col_df['Country'] = selected_holiday_col_df['Country'].str.strip()
    selected_holiday_col_df['From_date'] = pd.to_datetime(selected_holiday_col_df['From_date']).dt.date
    selected_holiday_col_df['to_date'] = pd.to_datetime(selected_holiday_col_df['to_date']).dt.date
    return selected_holiday_col_df


# %%
def getSelectedAirportCol(selected_airport_col_df):
    selected_airport_col_df=selected_airport_col_df[['AIRPORT_CODE','AIRPORT_NAME','COUNTRY_NAME',	'REGION_NAME']]
    return selected_airport_col_df


# %%
def getSelectedFlightCol(dataframe):
    selected_flights_colms_df=dataframe[['Flight_No','org','dst','SCH_DEP_DATE','BKD_WT_sum','BKD_VOL_sum','CHG_WT_BU_sum',
        'INHOUSE_AC_TYP',	'OPN_MODE',	'SVC_TYP',	'AC_CGO_WT_BU',	'AC_CGO_VOL_BU',
        'CMRCL_CGO_WT_BU',	'CMRCL_CGO_VOL_BU',	'NOOP_CAN_IND',	'ISO_CODE',	'EST_CGO_PLOD_WT_BU',
        'EST_CGO_PLOD_VOL_BU'
    ]]

    return selected_flights_colms_df

# %%
def loadData(fileName):
    dir=os.path.dirname(os.path.abspath("__file__"))
    #dir = os.path.dirname(__file__)
    print("abs---",dir)
    filename = dir+'\\data\\' + fileName;
    print("filename--",filename)
    return pd.read_csv(filename, low_memory=False,encoding='latin-1')  


# %%
flight_data=loadData("selectedFlightData.csv")
flight_data.head()
display(flight_data)
selected_flight_col_df=getSelectedFlightCol(flight_data)

parseDepartureDate(selected_flight_col_df)
holiday_data=loadData("2019HolidaysEventsCalendar.csv")
selected_holiday_col_df=getSelectedHolidayCol(holiday_data)
print("holiday count--",len(selected_holiday_col_df.index))

airport_data=loadData("airport_code.csv")
selected_aiport_col_df=getSelectedAirportCol(airport_data)
print("country count--",len(selected_aiport_col_df.index))


# %%

def joinOrgFlightAndContry(selected_flight_col_df,selected_aiport_col_df):
    
    flight_aiport_df=pd.merge(selected_flight_col_df,selected_aiport_col_df,how='left',left_on=['org'],right_on=        ['AIRPORT_CODE'])
    flight_aiport_df = flight_aiport_df.rename(columns={'COUNTRY_NAME': 'ORG_CNTRY_NAME',
                                'REGION_NAME':'ORG_REGION_NAME',
                                'AIRPORT_CODE':'ORG_AIRPORT_CODE',
                                'AIRPORT_NAME':'ORG_AIRPORT_NAME'})
    # display(flight_aiport_df)
    flight_aiport_df['ORG_CNTRY_NAME'] = flight_aiport_df['ORG_CNTRY_NAME'].str.upper()
    flight_aiport_df['ORG_CNTRY_NAME'] = flight_aiport_df['ORG_CNTRY_NAME'].str.strip()
    return flight_aiport_df
orgn_flight_contry_df=joinOrgFlightAndContry(selected_flight_col_df,selected_aiport_col_df)

# %% [markdown]
# 
# # Join destination and country master

# %%
def joinDstFlightAndContry(selected_flight_col_df,selected_aiport_col_df):
    flight_aiport_df=pd.merge(selected_flight_col_df,selected_aiport_col_df,how='left',left_on=['dst'],right_on=['AIRPORT_CODE'])
    flight_aiport_df = flight_aiport_df.rename(columns={'COUNTRY_NAME': 'DST_CNTRY_NAME',
                                'REGION_NAME':'DST_REGION_NAME',
                                'AIRPORT_CODE':'DST_AIRPORT_CODE',
                                'AIRPORT_NAME':'DST_AIRPORT_NAME'})
    flight_aiport_df['DST_CNTRY_NAME'] = flight_aiport_df['DST_CNTRY_NAME'].str.upper()
    flight_aiport_df['DST_CNTRY_NAME'] = flight_aiport_df['DST_CNTRY_NAME'].str.strip()                        
    return flight_aiport_df;
orgn_dst_flight_contry_df=joinDstFlightAndContry(orgn_flight_contry_df,selected_aiport_col_df)
    


# %%
def replaceNAN(flt_airpot_holiday_df):
    nan_count=flt_airpot_holiday_df.isna().sum().sum()
    print("NAN count--",nan_count)
    flt_airpot_holiday_df = flt_airpot_holiday_df.replace(np.nan, 0)
    nan_count=flt_airpot_holiday_df.isna().sum().sum()
    print("NAN count--",nan_count)
    return flt_airpot_holiday_df;


# %%
# def isHolidayInOrigin():


# %%



# %%

def joinFlighOrgAndHolidayData(orgn_dst_flight_contry_df,selected_holiday_col_df):
    flt_hlyday_flg_query = '''
        select flt.Flight_No,flt.org, flt.dst, flt.SCH_DEP_DATE, 1 as org_hday_flg
        from orgn_dst_flight_contry_df flt
        left join selected_holiday_col_df hldy 
        on flt.ORG_CNTRY_NAME=hldy.Country
        where flt.SCH_DEP_DATE >= hldy.From_date and flt.SCH_DEP_DATE <= hldy.to_date
        group by flt.org, flt.dst, flt.SCH_DEP_DATE,flt.Flight_No
    '''
    joined_flt_hlday_flag_df = ps.sqldf(flt_hlyday_flg_query,locals())

    final_flt_hlyday_query = '''
        select flt.*,coalesce(hldy.org_hday_flg,0) as org_hday_flg
        from orgn_dst_flight_contry_df flt
        left join joined_flt_hlday_flag_df hldy 
        on (flt.org=hldy.org 
            and flt.dst=hldy.dst 
            and flt.Flight_No=hldy.Flight_No 
            and flt.SCH_DEP_DATE=hldy.SCH_DEP_DATE
            )
    '''
    org_dst_flight_holidate_df = ps.sqldf(final_flt_hlyday_query,locals())

    return org_dst_flight_holidate_df

orgn_dst_flt_cntry_orgn_hlyday_df=joinFlighOrgAndHolidayData(orgn_dst_flight_contry_df,selected_holiday_col_df)
display(orgn_dst_flt_cntry_orgn_hlyday_df)
print("orgn holiday--",len(orgn_dst_flt_cntry_orgn_hlyday_df.index))
orgn_dst_flt_cntry_orgn_hlyday_df=orgn_dst_flt_cntry_orgn_hlyday_df.drop_duplicates()


# %%
def joinFlighDstAndHolidayData(orgn_dst_flight_contry_df,selected_holiday_col_df):
    # display(orgn_dst_flight_contry_df)
    # display(selected_holiday_col_df)
    
    flt_hlyday_flg_query = '''
        select flt.Flight_No,flt.org, flt.dst, flt.SCH_DEP_DATE, 1 as dst_hday_flg
        from orgn_dst_flight_contry_df flt
        left join selected_holiday_col_df hldy 
        on flt.DST_CNTRY_NAME=hldy.Country
        where flt.SCH_DEP_DATE >= hldy.From_date and flt.SCH_DEP_DATE <= hldy.to_date
        group by flt.org, flt.dst, flt.SCH_DEP_DATE,flt.Flight_No
    '''
    joined_flt_hlday_flag_df = ps.sqldf(flt_hlyday_flg_query,locals())

    final_flt_hlyday_query = '''
        select flt.*, coalesce(hldy.dst_hday_flg,0) as dst_hday_flg
        from orgn_dst_flight_contry_df flt
        left join joined_flt_hlday_flag_df hldy 
        on (flt.org=hldy.org 
            and flt.dst=hldy.dst 
            and flt.Flight_No=hldy.Flight_No 
            and flt.SCH_DEP_DATE=hldy.SCH_DEP_DATE
            )
    '''
    org_dst_flight_holidate_df = ps.sqldf(final_flt_hlyday_query,locals())
    return org_dst_flight_holidate_df

orgn_dst_flt_cntry_dstnorgn_hlyday_df=joinFlighDstAndHolidayData(orgn_dst_flt_cntry_orgn_hlyday_df,selected_holiday_col_df)
display(orgn_dst_flt_cntry_dstnorgn_hlyday_df)
print("orgn holiday--",len(orgn_dst_flt_cntry_dstnorgn_hlyday_df.index))

# %% [markdown]
# # Drop Columns

# %%
def dropColumns(flt_airpot_holiday_df):
    colm_array=['ORG_CNTRY_HOLIDAY','ORG_HOLIDAY_FROM_DATE','ORG_HOLIDAY_TO_DATE','DST_CNTRY_HOLIDAY',	    'DST_HOLIDAY_FROM_DATE','DST_HOLIDAY_TO_DATE','ORG_REGION_NAME','DST_REGION_NAME','ORG_AIRPORT_CODE',	'ORG_AIRPORT_NAME','ORG_CNTRY_NAME','DST_AIRPORT_CODE','DST_AIRPORT_NAME','DST_CNTRY_NAME']
    flt_airpot_holiday_df_droped=flt_airpot_holiday_df.drop(colm_array, axis = 1)
    return flt_airpot_holiday_df_droped;


# %%



# %%
# flt_airpot_holiday_drop_df=dropColumns(flt_airpot_holiday_df)
flt_airpot_holiday_drop_df=replaceNAN(orgn_dst_flt_cntry_dstnorgn_hlyday_df)
flt_airpot_holiday_drop_dup=flt_airpot_holiday_drop_df.drop_duplicates()
display(flt_airpot_holiday_drop_dup)


# %%
# Calculate Chargeable and Booked weight Ratio
def calEstimatedChgWeight(orgn_dst_flight_contry_df):
    orgn_dst_flight_contry_df.loc[(orgn_dst_flight_contry_df['CHG_WT_BU_sum'] <0)] = 1 
    orgn_dst_flight_contry_df.loc[(orgn_dst_flight_contry_df['BKD_WT_sum'] <0)] = 1 
    grp_org_dst_wt_query = '''
        select flt.org,flt.dst,sum(flt.CHG_WT_BU_sum)/sum(flt.BKD_WT_sum) as CHG_WT_RT
        from orgn_dst_flight_contry_df flt
        group by flt.org, flt.dst
    '''
    grpd_orgdst_chrgbl_rt_df = ps.sqldf(grp_org_dst_wt_query,locals())
    # grpd_orgdst_chrgbl_rt_df[CHG_WT_RT < 0] = 0
    print(grpd_orgdst_chrgbl_rt_df)
    grpd_orgdst_chrgbl_rt_df.loc[(grpd_orgdst_chrgbl_rt_df['CHG_WT_RT'] <0)] = 1 
    chrbl_cal_query = '''
        select flt.*,(flt.EST_CGO_PLOD_WT_BU * rt.CHG_WT_RT) as EST_CHG_WT
        from orgn_dst_flight_contry_df flt
        left join grpd_orgdst_chrgbl_rt_df rt 
        on (flt.org=rt.org 
            and flt.dst=rt.dst 
            )
        where flt.dst=rt.dst 
    '''
    grpd_orgdst_chrgbl_rt_df = ps.sqldf(chrbl_cal_query,locals())
    display(grpd_orgdst_chrgbl_rt_df)
    return grpd_orgdst_chrgbl_rt_df


grpd_orgdst_chrgbl_rt_df=calEstimatedChgWeight(flt_airpot_holiday_drop_dup);


# %%
def cargo_per_day(df):
    grp_fpt_dt_chg_df = df.groupby(['SCH_DEP_DATE'])['EST_CHG_WT'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(7,4))
    plt.hist(grp_fpt_dt_chg_df.EST_CHG_WT, color='mediumblue')
    
    ax.set(xlabel = "Cargo Per day",
           ylabel = "Count",
           title = "Distribution of Cargo Per Day")
# cargo_per_day(grpd_orgdst_chrgbl_rt_df)


# %%
def cargo_per_od(grpd_orgdst_chrgbl_rt_df):
    by_od = grpd_orgdst_chrgbl_rt_df.groupby(['org','dst'])['EST_CHG_WT'].sum().reset_index()
    print(by_od)
    fig, ax = plt.subplots(figsize=(7,4))
    sns.barplot(by_od.org+"-"+by_od.dst, by_od.EST_CHG_WT, color='mediumblue')
    
    ax.set(xlabel = "OD",
           ylabel = "Number of Cargo",
           title = "Total Cargo Per OD")
    
    sns.despine()
    
# cargo_per_od(grpd_orgdst_chrgbl_rt_df)

# create time series plot
def time_plot(data, x_col, y_col, title):

    fig, ax = plt.subplots(figsize=(15,5))
    sns.lineplot(x_col, y_col, data=data, ax=ax, color='mediumblue', label='Total Cargo')
    
    second = data.groupby(data.SCH_DEP_DATE)[y_col].mean().reset_index()
    second.date = pd.to_datetime(second.SCH_DEP_DATE, format='%Y-%m-%d')
    sns.lineplot(second.date, second[y_col], ax=ax, color='darkred', label='Average Cargo')
    
    ax.set(xlabel = "Date",
           ylabel = "Number of Cargo",
           title = title)
    
    sns.despine()
    





# %%
def time_plot(data, x_col, y_col, title):
    fig, ax = plt.subplots(figsize=(15,5))
    sns.lineplot(x_col, y_col, data=data, ax=ax, color='mediumblue', label='Total Cargo')
    
    # second = data.groupby(data.SCH_DEP_DATE)[y_col].mean().reset_index()
    # second.date = pd.to_datetime(second.SCH_DEP_DATE, format='%Y-%m-%d')
    # print(data)
    print("test--")
    data.SCH_DEP_DATE = pd.to_datetime(data.SCH_DEP_DATE)
    second = data.groupby(data.SCH_DEP_DATE.dt)[y_col].mean().reset_index()
    # print(second)
    second.date = pd.to_datetime(second.date, format="%Y-%m")
    # print(second)
    sns.lineplot((second.date + datetime.timedelta(6*365/12)), y_col, data=second, ax=ax, color='red', label='Mean Sales')  
    
    ax.set(xlabel = "Date",
           ylabel = "Cargo",
           title = title)
    sns.despine()
    
# time_plot(grpd_orgdst_chrgbl_rt_df, 'SCH_DEP_DATE', 'EST_CHG_WT', 'Daily Cargo Before Diff Transformation')


# %%
time_plot(grpd_orgdst_chrgbl_rt_df, 'SCH_DEP_DATE', 'EST_CHG_WT', 'Daily Cargo Before Diff Transformation')


# %%

def copyFinalDf(final_df):
    dir=os.path.dirname(os.path.abspath("__file__"))
    final_df.to_csv(dir+'/data/final_colm_output.csv')

copyFinalDf(flt_airpot_holiday_drop_df)


# %%



