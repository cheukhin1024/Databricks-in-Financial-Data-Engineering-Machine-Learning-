# Databricks notebook source
%sql
use deltabase

# COMMAND ----------

%sql
-- Use this when we need to manually vacuum
set spark.databricks.delta.retentionDurationCheck.enabled = False

-- Use this when we don't need to manually vacuum
--set spark.databricks.delta.retentionDurationCheck.enabled = True

# COMMAND ----------

%sql
--vacuum aap_30min_delta retain 0 hours dry run

vacuum aapl_30min_delta
vacuum aa_30min_delta
vacuum aal_30min_delta
vacuum aap_30min_delta
vacuum a_30min_delta
vacuum abbv_30min_delta 
vacuum abc_30min_delta 
vacuum abmd_30min_delta
vacuum abt_30min_delta
vacuum acn_30min_delta 
vacuum acv_30min_delta 
vacuum adbe_30min_delta
vacuum adi_30min_delta 
vacuum adm_30min_delta
vacuum adp_30min_delta
vacuum ads_30min_delta
vacuum adsk_30min_delta
vacuum adt_30min_delta 
vacuum aee_30min_delta 
vacuum aep_30min_delta 
vacuum aes_30min_delta 
vacuum afl_30min_delta 
vacuum aig_30min_delta 
vacuum ainv_30min_delta
vacuum aiv_30min_delta 
vacuum aiz_30min_delta 
vacuum ajg_30min_delta 
vacuum akam_30min_delta 
vacuum alb_30min_delta 
vacuum algn_30min_delta 
vacuum alk_30min_delta
vacuum all_30min_delta
vacuum alle_30min_delta 
vacuum altr_30min_delta 
vacuum amat_30min_delta
vacuum ambc_30min_delta
vacuum amcr_30min_delta 
vacuum amd_30min_delta 
vacuum ame_30min_delta
vacuum amg_30min_delta
vacuum amgn_30min_delta
vacuum amp_30min_delta
vacuum amt_30min_delta 
vacuum amzn_30min_delta 
vacuum an_30min_delta
vacuum anet_30min_delta
vacuum anf_30min_delta
vacuum anss_30min_delta 
vacuum antm_30min_delta
vacuum aon_30min_delta 
vacuum aos_30min_delta 
vacuum apa_30min_delta 
vacuum apd_30min_delta 
vacuum aph_30min_delta 
vacuum aptv_30min_delta 
vacuum are_30min_delta 
vacuum arnc_30min_delta 
vacuum ash_30min_delta 
vacuum aso_30min_delta 
vacuum atge_30min_delta 
vacuum ati_30min_delta 
vacuum ato_30min_delta 
vacuum atvi_30min_delta 
vacuum avb_30min_delta 
vacuum avgo_30min_delta 
vacuum avy_30min_delta 
vacuum awk_30min_delta 
vacuum axp_30min_delta 
vacuum ayi_30min_delta 
vacuum azo_30min_delta 
vacuum ba_30min_delta 
vacuum bac_30min_delta 
vacuum bax_30min_delta 
vacuum bbby_30min_delta
vacuum bby_30min_delta 
vacuum bc_30min_delta 
vacuum bdx_30min_delta 
vacuum ben_30min_delta 
vacuum bfb_30min_delta 
vacuum bidu_30min_delta 
vacuum big_30min_delta
vacuum biib_30min_delta 
vacuum bio_30min_delta 
vacuum bk_30min_delta 
vacuum bkng_30min_delta 
vacuum blk_30min_delta 
vacuum bll_30min_delta 
vacuum bmrn_30min_delta 
vacuum bmy_30min_delta 
vacuum br_30min_delta 
vacuum brkb_30min_delta 
vacuum bro_30min_delta 
vacuum bsx_30min_delta 
vacuum btu_30min_delta 
vacuum bud_30min_delta 
vacuum bwa_30min_delta 
      vacuum bxp_30min_delta 
      vacuum c_30min_delta 
      vacuum cag_30min_delta 
      vacuum cah_30min_delta 
      vacuum car_30min_delta
      vacuum carr_30min_delta 
      vacuum cat_30min_delta 
      vacuum cb_30min_delta 
      vacuum cbh_30min_delta 
      vacuum cboe_30min_delta 
      vacuum cbre_30min_delta
      vacuum cc_30min_delta
      vacuum cci_30min_delta
      vacuum cck_30min_delta
      vacuum ccl_30min_delta 
      vacuum ccu_30min_delta
      vacuum cday_30min_delta 
      vacuum cdns_30min_delta 
      vacuum cdw_30min_delta 
      vacuum ce_30min_delta 
      vacuum cern_30min_delta 
      vacuum cf_30min_delta 
      vacuum cfg_30min_delta 
      vacuum chd_30min_delta 
      vacuum chir_30min_delta 
      vacuum chk_30min_delta 
      vacuum chkp_30min_delta 
      vacuum chrw_30min_delta 
      vacuum chtr_30min_delta
      vacuum ci_30min_delta 
      vacuum cien_30min_delta 
      vacuum cinf_30min_delta 
      vacuum cit_30min_delta 
      vacuum cl_30min_delta 
      vacuum clf_30min_delta 
      vacuum clx_30min_delta 
      vacuum cma_30min_delta 
      vacuum cmcsa_30min_delta 
      vacuum cme_30min_delta 
      vacuum cmg_30min_delta 
      vacuum cmi_30min_delta 
      vacuum cms_30min_delta 
      vacuum cnc_30min_delta 
      vacuum cnp_30min_delta 
      vacuum cnx_30min_delta 
      vacuum cof_30min_delta 
      vacuum coo_30min_delta 
      vacuum coop_30min_delta 
      vacuum cop_30min_delta 
      vacuum cost_30min_delta
      vacuum coty_30min_delta 
      vacuum cpb_30min_delta 
      vacuum cpri_30min_delta
      vacuum cprt_30min_delta
      vacuum cpt_30min_delta
      vacuum crm_30min_delta 
      vacuum csco_30min_delta 
      vacuum csx_30min_delta 
      vacuum ctas_30min_delta 
      vacuum ctlt_30min_delta
      vacuum ctsh_30min_delta
      vacuum ctva_30min_delta 
      vacuum ctxs_30min_delta 
      vacuum cvs_30min_delta
      vacuum cvx_30min_delta 
      vacuum czr_30min_delta 
      vacuum d_30min_delta 
      vacuum dal_30min_delta
      vacuum dan_30min_delta
      vacuum dd_30min_delta 
      vacuum dds_30min_delta 
      vacuum de_30min_delta 
      vacuum dell_30min_delta 
      vacuum dfs_30min_delta
      vacuum dg_30min_delta 
      vacuum dgx_30min_delta 
      vacuum dhi_30min_delta
      vacuum dhr_30min_delta
      vacuum dis_30min_delta 
      vacuum disca_30min_delta 
      vacuum disck_30min_delta 
      vacuum dish_30min_delta 
      vacuum dlr_30min_delta 
      vacuum dltr_30min_delta 
      vacuum dlx_30min_delta
      vacuum dnb_30min_delta 
      vacuum dov_30min_delta
      vacuum dow_30min_delta 
      vacuum dpz_30min_delta
      vacuum dre_30min_delta 
      vacuum dri_30min_delta 
      vacuum dte_30min_delta 
      vacuum duk_30min_delta
      vacuum dva_30min_delta 
      vacuum dvn_30min_delta
      vacuum dxc_30min_delta 
      vacuum dxcm_30min_delta 
      vacuum ea_30min_delta 
      vacuum ebay_30min_delta 
      vacuum ecl_30min_delta 
      vacuum ed_30min_delta 
      vacuum efx_30min_delta
      vacuum eix_30min_delta
      vacuum el_30min_delta 
      vacuum emn_30min_delta
      vacuum emr_30min_delta 
      vacuum endp_30min_delta 
      vacuum enph_30min_delta 
      vacuum eog_30min_delta
      vacuum epam_30min_delta 
      vacuum eq_30min_delta
      vacuum eqix_30min_delta 
      vacuum eqr_30min_delta
      vacuum eqt_30min_delta 
      vacuum es_30min_delta 
      vacuum ess_30min_delta 
      vacuum etn_30min_delta 
      vacuum etr_30min_delta 
      vacuum etsy_30min_delta
      vacuum evrg_30min_delta
      vacuum ew_30min_delta 
      vacuum exc_30min_delta 
      vacuum expd_30min_delta 
      vacuum expe_30min_delta 
      vacuum exr_30min_delta 
      vacuum f_30min_delta 
      vacuum fang_30min_delta 
      vacuum fast_30min_delta
      vacuum fb_30min_delta 
      vacuum fbhs_30min_delta 
      vacuum fcx_30min_delta
      vacuum fds_30min_delta 
      vacuum fdx_30min_delta 
      vacuum fe_30min_delta
      vacuum ffiv_30min_delta
      vacuum fhn_30min_delta 
      vacuum fis_30min_delta 
      vacuum fisv_30min_delta 
      vacuum fitb_30min_delta 
      vacuum fl_30min_delta 
      vacuum flex_30min_delta
      vacuum flr_30min_delta
      vacuum fls_30min_delta 
      vacuum flt_30min_delta 
      vacuum fmc_30min_delta 
      vacuum fosl_30min_delta
      vacuum fox_30min_delta 
      vacuum foxa_30min_delta 
      vacuum fpl_30min_delta 
      vacuum frc_30min_delta
      vacuum frt_30min_delta 
      vacuum fslr_30min_delta
      vacuum fti_30min_delta 
      vacuum ftnt_30min_delta 
      vacuum ftv_30min_delta 
      vacuum gci_30min_delta 
      vacuum gd_30min_delta
      vacuum ge_30min_delta 
      vacuum ghc_30min_delta
      vacuum gild_30min_delta
      vacuum gis_30min_delta 
      vacuum gl_30min_delta 
      vacuum glw_30min_delta 
      vacuum gm_30min_delta 
      vacuum gme_30min_delta 
      vacuum gnrc_30min_delta 
      vacuum gnw_30min_delta 
      vacuum goog_30min_delta 
      vacuum googl_30min_delta 
      vacuum gp_30min_delta 
      vacuum gpc_30min_delta 
      vacuum gpn_30min_delta
      vacuum gps_30min_delta 
      vacuum grmn_30min_delta 
      vacuum gs_30min_delta
      vacuum gt_30min_delta 
      vacuum gww_30min_delta
      vacuum hal_30min_delta 
      vacuum has_30min_delta 
      vacuum hban_30min_delta 
      vacuum hbi_30min_delta 
      vacuum hca_30min_delta 
      vacuum hd_30min_delta 
      vacuum hes_30min_delta 
      vacuum hfc_30min_delta 
      vacuum hig_30min_delta 
      vacuum hii_30min_delta 
      vacuum hlt_30min_delta 
      vacuum hog_30min_delta 
      vacuum holx_30min_delta 
      vacuum hon_30min_delta 
      vacuum hp_30min_delta 
      vacuum hpe_30min_delta
      vacuum hpq_30min_delta 
      vacuum hrb_30min_delta 
      vacuum hrl_30min_delta 
      vacuum hsic_30min_delta 
      vacuum hst_30min_delta 
      vacuum hsy_30min_delta 
      vacuum hum_30min_delta
      vacuum iac_30min_delta 
      vacuum ibm_30min_delta 
      vacuum ice_30min_delta
      vacuum idxx_30min_delta 
      vacuum iex_30min_delta 
      vacuum iff_30min_delta 
      vacuum igt_30min_delta 
      vacuum ihrt_30min_delta 
      vacuum ilmn_30min_delta
      vacuum incy_30min_delta 
      vacuum info_30min_delta 
      vacuum infy_30min_delta
      vacuum intc_30min_delta 
      vacuum intu_30min_delta 
      vacuum ip_30min_delta 
      vacuum ipg_30min_delta
      vacuum ipgp_30min_delta 
      vacuum iqv_30min_delta 
      vacuum ir_30min_delta 
      vacuum irm_30min_delta
      vacuum isrg_30min_delta
      vacuum it_30min_delta 
      vacuum itt_30min_delta 
      vacuum itw_30min_delta 
      vacuum ivz_30min_delta 
      vacuum j_30min_delta 
      vacuum jbht_30min_delta 
      vacuum jbl_30min_delta 
      vacuum jci_30min_delta
      vacuum jd_30min_delta
      vacuum jef_30min_delta 
      vacuum jkhy_30min_delta 
      vacuum jnj_30min_delta 
      vacuum jnpr_30min_delta 
      vacuum jp_30min_delta 
      vacuum jpm_30min_delta 
      vacuum jwn_30min_delta 
      vacuum k_30min_delta
      vacuum kbh_30min_delta 
      vacuum key_30min_delta 
      vacuum keys_30min_delta
      vacuum khc_30min_delta 
      vacuum kim_30min_delta 
      vacuum klac_30min_delta
      vacuum kmb_30min_delta 
      vacuum kmi_30min_delta
      vacuum kmx_30min_delta 
      vacuum ko_30min_delta 
      vacuum kodk_30min_delta 
      vacuum kr_30min_delta 
      vacuum kss_30min_delta 
      vacuum ksu_30min_delta
      vacuum l_30min_delta 
      vacuum lbtyk_30min_delta 
      vacuum ldos_30min_delta 
      vacuum leg_30min_delta 
      vacuum len_30min_delta 
      vacuum lh_30min_delta 
      vacuum lhx_30min_delta 
      vacuum life_30min_delta 
      vacuum lin_30min_delta 
      vacuum lkq_30min_delta 
      vacuum lly_30min_delta 
      vacuum lmt_30min_delta 
      vacuum lnc_30min_delta 
      vacuum lnt_30min_delta 
      vacuum logi_30min_delta 
      vacuum low_30min_delta 
      vacuum lrcx_30min_delta 
      vacuum lsi_30min_delta 
      vacuum lu_30min_delta
      vacuum lumn_30min_delta
      vacuum luv_30min_delta 
      vacuum lvs_30min_delta 
      vacuum lw_30min_delta 
      vacuum lyb_30min_delta 
      vacuum lyv_30min_delta 
      vacuum m_30min_delta 
      vacuum ma_30min_delta 
      vacuum maa_30min_delta
      vacuum mac_30min_delta 
      vacuum mar_30min_delta
      vacuum mas_30min_delta 
      vacuum mat_30min_delta 
      vacuum mbi_30min_delta 
      vacuum mcd_30min_delta 
      vacuum mchp_30min_delta
      vacuum mck_30min_delta
      vacuum mco_30min_delta 
      vacuum mdlz_30min_delta 
      vacuum mdp_30min_delta 
      vacuum mdt_30min_delta 
      vacuum met_30min_delta 
      vacuum mgm_30min_delta 
      vacuum mhk_30min_delta 
      vacuum mkc_30min_delta 
      vacuum mktx_30min_delta 
      vacuum mlm_30min_delta 
      vacuum mmc_30min_delta 
      vacuum mmi_30min_delta 
      vacuum mmm_30min_delta 
      vacuum mnst_30min_delta 
      vacuum mo_30min_delta 
      vacuum moh_30min_delta 
      vacuum mos_30min_delta 
      vacuum mpc_30min_delta 
      vacuum mpwr_30min_delta 
      vacuum mrk_30min_delta 
      vacuum mro_30min_delta 
      vacuum mrvl_30min_delta 
      vacuum ms_30min_delta 
      vacuum msci_30min_delta 
      vacuum msft_30min_delta 
      vacuum msi_30min_delta 
      vacuum mtb_30min_delta 
      vacuum mtch_30min_delta 
      vacuum mtd_30min_delta 
      vacuum mtw_30min_delta 
      vacuum mu_30min_delta 
      vacuum mur_30min_delta 
      vacuum navi_30min_delta 
      vacuum nbr_30min_delta 
      vacuum nclh_30min_delta 
      vacuum ndaq_30min_delta 
      vacuum ndsn_30min_delta 
      vacuum ne_30min_delta 
      vacuum nee_30min_delta 
      vacuum nem_30min_delta 
      vacuum nflx_30min_delta 
      vacuum ni_30min_delta 
      vacuum nke_30min_delta 
      vacuum nktr_30min_delta
      vacuum nlok_30min_delta 
      vacuum nlsn_30min_delta 
      vacuum noc_30min_delta 
      vacuum nov_30min_delta
      vacuum now_30min_delta 
      vacuum nrg_30min_delta 
      vacuum nsc_30min_delta 
      vacuum ntap_30min_delta 
      vacuum ntes_30min_delta 
      vacuum ntrs_30min_delta 
      vacuum nue_30min_delta 
      vacuum nvda_30min_delta
      vacuum nvr_30min_delta 
      vacuum nwl_30min_delta 
      vacuum nws_30min_delta 
      vacuum nwsa_30min_delta 
      vacuum nxpi_30min_delta 
      vacuum nyt_30min_delta 
      vacuum o_30min_delta 
      vacuum odfl_30min_delta 
      vacuum odp_30min_delta 
      vacuum ogn_30min_delta
      vacuum oi_30min_delta 
      vacuum oke_30min_delta
      vacuum omc_30min_delta 
      vacuum one_30min_delta 
      vacuum orcl_30min_delta 
      vacuum orly_30min_delta 
      vacuum otis_30min_delta
      vacuum oxy_30min_delta 
      vacuum par_30min_delta
      vacuum payc_30min_delta 
      vacuum payx_30min_delta
      vacuum pbct_30min_delta 
      vacuum pbi_30min_delta 
      vacuum pcar_30min_delta 
      vacuum pcg_30min_delta 
      vacuum pdco_30min_delta 
      vacuum peak_30min_delta
      vacuum peg_30min_delta 
      vacuum penn_30min_delta 
      vacuum pep_30min_delta 
      vacuum pfe_30min_delta
      vacuum pfg_30min_delta 
      vacuum pg_30min_delta 
      vacuum pgr_30min_delta 
      vacuum ph_30min_delta 
      vacuum phm_30min_delta 
      vacuum pkg_30min_delta 
      vacuum pki_30min_delta 
      vacuum pld_30min_delta
      vacuum pll_30min_delta 
      vacuum pm_30min_delta 
      vacuum pnc_30min_delta 
      vacuum pnr_30min_delta 
      vacuum pnw_30min_delta 
      vacuum pool_30min_delta 
      vacuum ppg_30min_delta
      vacuum ppl_30min_delta 
      vacuum prgo_30min_delta
      vacuum pri_30min_delta 
      vacuum pru_30min_delta 
      vacuum psa_30min_delta 
      vacuum psx_30min_delta 
      vacuum ptc_30min_delta 
      vacuum pvh_30min_delta 
      vacuum pwr_30min_delta 
      vacuum pxd_30min_delta 
      vacuum pypl_30min_delta
      vacuum qcom_30min_delta 
      vacuum qgen_30min_delta 
      vacuum qrvo_30min_delta 
      vacuum r_30min_delta 
      vacuum rcl_30min_delta 
      vacuum re_30min_delta 
      vacuum reg_30min_delta
      vacuum regn_30min_delta 
      vacuum rf_30min_delta
      vacuum rhi_30min_delta 
      vacuum rig_30min_delta
      vacuum rjf_30min_delta 
      vacuum rl_30min_delta 
      vacuum rlgy_30min_delta 
      vacuum rmd_30min_delta
      vacuum rok_30min_delta 
      vacuum rol_30min_delta 
      vacuum rop_30min_delta 
      vacuum rost_30min_delta 
      vacuum rrc_30min_delta 
      vacuum rrd_30min_delta 
      vacuum rsg_30min_delta 
      vacuum rtx_30min_delta 
      vacuum ryaay_30min_delta 
      vacuum s_30min_delta 
      vacuum saic_30min_delta 
      vacuum sanm_30min_delta 
      vacuum sbac_30min_delta 
      vacuum sbny_30min_delta
      vacuum sbux_30min_delta 
      vacuum schw_30min_delta 
      vacuum se_30min_delta 
      vacuum sedg_30min_delta 
      vacuum see_30min_delta 
      vacuum shw_30min_delta 
      vacuum sig_30min_delta 
      vacuum siri_30min_delta 
      vacuum sitc_30min_delta 
      vacuum sivb_30min_delta 
      vacuum sjm_30min_delta  
      vacuum slb_30min_delta 
      vacuum slg_30min_delta 
      vacuum slm_30min_delta 
      vacuum sna_30min_delta 
      vacuum snps_30min_delta 
      vacuum so_30min_delta
      vacuum spg_30min_delta 
      vacuum spgi_30min_delta 
      vacuum srcl_30min_delta 
      vacuum sre_30min_delta 
      vacuum ssp_30min_delta 
      vacuum ste_30min_delta 
      vacuum stt_30min_delta 
      vacuum stx_30min_delta 
      vacuum stz_30min_delta 
      vacuum sun_30min_delta 
      vacuum swk_30min_delta 
      vacuum swks_30min_delta 
      vacuum swn_30min_delta 
      vacuum syf_30min_delta
      vacuum syk_30min_delta 
      vacuum syy_30min_delta 
      vacuum t_30min_delta 
      vacuum tap_30min_delta 
      vacuum tdc_30min_delta 
      vacuum tdg_30min_delta 
      vacuum tdy_30min_delta 
      vacuum tel_30min_delta 
      vacuum ter_30min_delta 
      vacuum teva_30min_delta 
      vacuum tex_30min_delta 
      vacuum tfc_30min_delta 
      vacuum tfx_30min_delta 
      vacuum tgna_30min_delta 
      vacuum tgt_30min_delta 
      vacuum thc_30min_delta 
      vacuum tjx_30min_delta 
      vacuum tmo_30min_delta 
      vacuum tmus_30min_delta 
      vacuum tpr_30min_delta 
      vacuum trip_30min_delta 
      vacuum trmb_30min_delta 
      vacuum trow_30min_delta 
      vacuum trv_30min_delta 
      vacuum tsco_30min_delta 
      vacuum tsla_30min_delta 
      vacuum tsn_30min_delta 
      vacuum ttwo_30min_delta
      vacuum tup_30min_delta 
      vacuum twtr_30min_delta 
      vacuum txn_30min_delta 
      vacuum txt_30min_delta
      vacuum tyl_30min_delta 
      vacuum ua_30min_delta 
      vacuum uaa_30min_delta 
      vacuum ual_30min_delta 
      vacuum ucl_30min_delta 
      vacuum udr_30min_delta 
      vacuum uhs_30min_delta 
      vacuum ulta_30min_delta 
      vacuum unh_30min_delta 
      vacuum unm_30min_delta 
      vacuum unp_30min_delta 
      vacuum upc_30min_delta 
      vacuum ups_30min_delta 
      vacuum urbn_30min_delta
      vacuum uri_30min_delta 
      vacuum usb_30min_delta 
      vacuum v_30min_delta 
      vacuum val_30min_delta
      vacuum vfc_30min_delta 
      vacuum viav_30min_delta
      vacuum vlo_30min_delta 
      vacuum vmc_30min_delta 
      vacuum vno_30min_delta 
      vacuum vnt_30min_delta 
      vacuum vod_30min_delta 
      vacuum vrsk_30min_delta 
      vacuum vrsn_30min_delta 
      vacuum vrts_30min_delta 
      vacuum vrtx_30min_delta 
      vacuum vtr_30min_delta 
      vacuum vtrs_30min_delta 
      vacuum vz_30min_delta 
      vacuum wab_30min_delta 
      vacuum wat_30min_delta 
      vacuum wba_30min_delta 
      vacuum wdc_30min_delta 
      vacuum wec_30min_delta 
      vacuum well_30min_delta 
      vacuum wfc_30min_delta 
      vacuum whr_30min_delta 
      vacuum wltw_30min_delta 
      vacuum wm_30min_delta 
      vacuum wmb_30min_delta 
      vacuum wmt_30min_delta 
      vacuum wor_30min_delta 
      vacuum wrb_30min_delta 
      vacuum wrk_30min_delta 
      vacuum wst_30min_delta 
      vacuum wu_30min_delta 
      vacuum wy_30min_delta 
      vacuum wynn_30min_delta 
      vacuum x_30min_delta 
      vacuum xel_30min_delta 
      vacuum xlnx_30min_delta 
      vacuum xom_30min_delta 
      vacuum xray_30min_delta 
      vacuum xrx_30min_delta 
      vacuum xyl_30min_delta 
      vacuum yum_30min_delta 
      vacuum zbh_30min_delta 
      vacuum zbra_30min_delta 
      vacuum zion_30min_delta 
      vacuum zts_30min_delta

# COMMAND ----------

%sql
vacuum aapl_30min_delta dry run
vacuum aa_30min_delta dry run
vacuum aal_30min_delta dry run
vacuum aap_30min_delta dry run
vacuum a_30min_delta dry run
vacuum abbv_30min_delta dry run
vacuum abc_30min_delta dry run
vacuum abmd_30min_delta dry run
vacuum abt_30min_delta dry run
vacuum acn_30min_delta dry run
vacuum acv_30min_delta dry run
vacuum adbe_30min_delta dry run
vacuum adi_30min_delta dry run
vacuum adm_30min_delta dry run
vacuum adp_30min_delta dry run
vacuum ads_30min_delta dry run
vacuum adsk_30min_delta dry run
vacuum adt_30min_delta dry run
vacuum aee_30min_delta dry run
vacuum aep_30min_delta dry run
vacuum aes_30min_delta dry run
vacuum afl_30min_delta dry run 
vacuum aig_30min_delta dry run
vacuum ainv_30min_delta dry run
vacuum aiv_30min_delta dry run
vacuum aiz_30min_delta dry run
vacuum ajg_30min_delta  dry run
vacuum akam_30min_delta dry run
vacuum alb_30min_delta  dry run
vacuum algn_30min_delta dry run
vacuum alk_30min_delta dry run
vacuum all_30min_delta dry run
vacuum alle_30min_delta dry run
vacuum altr_30min_delta dry run
vacuum amat_30min_delta dry run
vacuum ambc_30min_delta dry run
vacuum amcr_30min_delta dry run
vacuum amd_30min_delta dry run
vacuum ame_30min_delta dry run
vacuum amg_30min_delta dry run
vacuum amgn_30min_delta dry run
vacuum amp_30min_delta dry run
vacuum amt_30min_delta  dry run
vacuum amzn_30min_delta  dry run
vacuum an_30min_delta dry run
vacuum anet_30min_delta dry run
vacuum anf_30min_delta dry run
vacuum anss_30min_delta  dry run
vacuum antm_30min_delta dry run
vacuum aon_30min_delta  dry run
vacuum aos_30min_delta  dry run
vacuum apa_30min_delta  dry run
vacuum apd_30min_delta  dry run
vacuum aph_30min_delta  dry run
vacuum aptv_30min_delta  dry run
vacuum are_30min_delta  dry run
vacuum arnc_30min_delta  dry run
vacuum ash_30min_delta  dry run
vacuum aso_30min_delta  dry run
vacuum atge_30min_delta  dry run
vacuum ati_30min_delta  dry run
vacuum ato_30min_delta  dry run
vacuum atvi_30min_delta  dry run
vacuum avb_30min_delta  dry run
vacuum avgo_30min_delta  dry run
vacuum avy_30min_delta  dry run
vacuum awk_30min_delta  dry run
vacuum axp_30min_delta  dry run
vacuum ayi_30min_delta  dry run
vacuum azo_30min_delta  dry run
vacuum ba_30min_delta  dry run
vacuum bac_30min_delta  dry run
vacuum bax_30min_delta  dry run
vacuum bbby_30min_delta dry run
vacuum bby_30min_delta  dry run
vacuum bc_30min_delta  dry run
vacuum bdx_30min_delta  dry run
vacuum ben_30min_delta  dry run
vacuum bfb_30min_delta  dry run
vacuum bidu_30min_delta  dry run
vacuum big_30min_delta dry run
vacuum biib_30min_delta  dry run
vacuum bio_30min_delta  dry run
vacuum bk_30min_delta  dry run
vacuum bkng_30min_delta  dry run
vacuum blk_30min_delta  dry run
vacuum bll_30min_delta  dry run
vacuum bmrn_30min_delta  dry run
vacuum bmy_30min_delta  dry run
vacuum br_30min_delta  dry run
vacuum brkb_30min_delta  dry run
vacuum bro_30min_delta  dry run
vacuum bsx_30min_delta  dry run
vacuum btu_30min_delta  dry run
vacuum bud_30min_delta  dry run
vacuum bwa_30min_delta  dry run
      vacuum bxp_30min_delta  dry run
      vacuum c_30min_delta  dry run
      vacuum cag_30min_delta  dry run
      vacuum cah_30min_delta  dry run
      vacuum car_30min_delta dry run
      vacuum carr_30min_delta  dry run
      vacuum cat_30min_delta  dry run
      vacuum cb_30min_delta  dry run
      vacuum cbh_30min_delta  dry run
      vacuum cboe_30min_delta  dry run
      vacuum cbre_30min_delta dry run
      vacuum cc_30min_delta dry run
      vacuum cci_30min_delta dry run
      vacuum cck_30min_delta dry run
      vacuum ccl_30min_delta  dry run
      vacuum ccu_30min_delta dry run
      vacuum cday_30min_delta  dry run
      vacuum cdns_30min_delta  dry run
      vacuum cdw_30min_delta  dry run
      vacuum ce_30min_delta  dry run
      vacuum cern_30min_delta  dry run
      vacuum cf_30min_delta  dry run
      vacuum cfg_30min_delta  dry run
      vacuum chd_30min_delta  dry run
      vacuum chir_30min_delta  dry run
      vacuum chk_30min_delta  dry run
      vacuum chkp_30min_delta  dry run
      vacuum chrw_30min_delta  dry run
      vacuum chtr_30min_delta dry run
      vacuum ci_30min_delta  dry run
      vacuum cien_30min_delta  dry run
      vacuum cinf_30min_delta  dry run
      vacuum cit_30min_delta  dry run
      vacuum cl_30min_delta  dry run
      vacuum clf_30min_delta  dry run
      vacuum clx_30min_delta  dry run
      vacuum cma_30min_delta  dry run
      vacuum cmcsa_30min_delta  dry run
      vacuum cme_30min_delta  dry run
      vacuum cmg_30min_delta  dry run
      vacuum cmi_30min_delta  dry run
      vacuum cms_30min_delta  dry run
      vacuum cnc_30min_delta  dry run
      vacuum cnp_30min_delta  dry run
      vacuum cnx_30min_delta  dry run
      vacuum cof_30min_delta  dry run
      vacuum coo_30min_delta  dry run
      vacuum coop_30min_delta  dry run
      vacuum cop_30min_delta  dry run
      vacuum cost_30min_delta dry run
      vacuum coty_30min_delta  dry run
      vacuum cpb_30min_delta  dry run
      vacuum cpri_30min_delta dry run 
      vacuum cprt_30min_delta dry run
      vacuum cpt_30min_delta dry run
      vacuum crm_30min_delta  dry run
      vacuum csco_30min_delta  dry run
      vacuum csx_30min_delta  dry run
      vacuum ctas_30min_delta  dry run
      vacuum ctlt_30min_delta dry run
      vacuum ctsh_30min_delta dry run
      vacuum ctva_30min_delta  dry run
      vacuum ctxs_30min_delta  dry run
      vacuum cvs_30min_delta dry run
      vacuum cvx_30min_delta  dry run
      vacuum czr_30min_delta  dry run
      vacuum d_30min_delta  dry run
      vacuum dal_30min_delta dry run
      vacuum dan_30min_delta dry run
      vacuum dd_30min_delta  dry run
      vacuum dds_30min_delta  dry run
      vacuum de_30min_delta  dry run
      vacuum dell_30min_delta  dry run
      vacuum dfs_30min_delta dry run
      vacuum dg_30min_delta  dry run
      vacuum dgx_30min_delta  dry run
      vacuum dhi_30min_delta dry run
      vacuum dhr_30min_delta dry run
      vacuum dis_30min_delta  dry run
      vacuum disca_30min_delta  dry run
      vacuum disck_30min_delta  dry run
      vacuum dish_30min_delta  dry run
      vacuum dlr_30min_delta  dry run
      vacuum dltr_30min_delta  dry run
      vacuum dlx_30min_delta dry run
      vacuum dnb_30min_delta  dry run
      vacuum dov_30min_delta dry run
      vacuum dow_30min_delta  dry run
      vacuum dpz_30min_delta dry run
      vacuum dre_30min_delta  dry run
      vacuum dri_30min_delta  dry run
      vacuum dte_30min_delta  dry run
      vacuum duk_30min_delta dry run
      vacuum dva_30min_delta  dry run
      vacuum dvn_30min_delta dry run
      vacuum dxc_30min_delta  dry run
      vacuum dxcm_30min_delta  dry run
      vacuum ea_30min_delta  dry run
      vacuum ebay_30min_delta  dry run
      vacuum ecl_30min_delta  dry run
      vacuum ed_30min_delta  dry run
      vacuum efx_30min_delta dry run
      vacuum eix_30min_delta dry run
      vacuum el_30min_delta  dry run
      vacuum emn_30min_delta dry run
      vacuum emr_30min_delta  dry run
      vacuum endp_30min_delta  dry run
      vacuum enph_30min_delta  dry run
      vacuum eog_30min_delta dry run
      vacuum epam_30min_delta  dry run
      vacuum eq_30min_delta dry run
      vacuum eqix_30min_delta  dry run
      vacuum eqr_30min_delta dry run
      vacuum eqt_30min_delta  dry run
      vacuum es_30min_delta  dry run
      vacuum ess_30min_delta  dry run
      vacuum etn_30min_delta  dry run
      vacuum etr_30min_delta  dry run
      vacuum etsy_30min_delta dry run
      vacuum evrg_30min_delta dry run
      vacuum ew_30min_delta  dry run
      vacuum exc_30min_delta  dry run
      vacuum expd_30min_delta  dry run
      vacuum expe_30min_delta  dry run
      vacuum exr_30min_delta  dry run
      vacuum f_30min_delta  dry run
      vacuum fang_30min_delta  dry run
      vacuum fast_30min_delta dry run
      vacuum fb_30min_delta  dry run
      vacuum fbhs_30min_delta  dry run
      vacuum fcx_30min_delta dry run
      vacuum fds_30min_delta  dry run
      vacuum fdx_30min_delta  dry run
      vacuum fe_30min_delta dry run
      vacuum ffiv_30min_delta dry run
      vacuum fhn_30min_delta  dry run
      vacuum fis_30min_delta  dry run
      vacuum fisv_30min_delta  dry run
      vacuum fitb_30min_delta  dry run
      vacuum fl_30min_delta  dry run
      vacuum flex_30min_delta dry run
      vacuum flr_30min_delta dry run
      vacuum fls_30min_delta  dry run
      vacuum flt_30min_delta  dry run
      vacuum fmc_30min_delta  dry run
      vacuum fosl_30min_delta dry run
      vacuum fox_30min_delta  dry run
      vacuum foxa_30min_delta  dry run
      vacuum fpl_30min_delta  dry run
      vacuum frc_30min_delta dry run
      vacuum frt_30min_delta  dry run
      vacuum fslr_30min_delta dry run
      vacuum fti_30min_delta  dry run
      vacuum ftnt_30min_delta  dry run
      vacuum ftv_30min_delta  dry run
      vacuum gci_30min_delta  dry run
      vacuum gd_30min_delta dry run
      vacuum ge_30min_delta  dry run
      vacuum ghc_30min_delta dry run
      vacuum gild_30min_delta dry run
      vacuum gis_30min_delta  dry run
      vacuum gl_30min_delta  dry run
      vacuum glw_30min_delta  dry run
      vacuum gm_30min_delta  dry run
      vacuum gme_30min_delta  dry run
      vacuum gnrc_30min_delta  dry run
      vacuum gnw_30min_delta  dry run
      vacuum goog_30min_delta  dry run
      vacuum googl_30min_delta  dry run
      vacuum gp_30min_delta  dry run
      vacuum gpc_30min_delta  dry run
      vacuum gpn_30min_delta dry run
      vacuum gps_30min_delta  dry run
      vacuum grmn_30min_delta  dry run
      vacuum gs_30min_delta dry run
      vacuum gt_30min_delta  dry run
      vacuum gww_30min_delta dry run
      vacuum hal_30min_delta  dry run
      vacuum has_30min_delta  dry run
      vacuum hban_30min_delta  dry run
      vacuum hbi_30min_delta  dry run
      vacuum hca_30min_delta  dry run
      vacuum hd_30min_delta  dry run
      vacuum hes_30min_delta  dry run
      vacuum hfc_30min_delta  dry run
      vacuum hig_30min_delta  dry run
      vacuum hii_30min_delta  dry run
      vacuum hlt_30min_delta  dry run
      vacuum hog_30min_delta  dry run
      vacuum holx_30min_delta  dry run
      vacuum hon_30min_delta  dry run
      vacuum hp_30min_delta  dry run
      vacuum hpe_30min_delta dry run
      vacuum hpq_30min_delta  dry run
      vacuum hrb_30min_delta  dry run
      vacuum hrl_30min_delta  dry run
      vacuum hsic_30min_delta  dry run
      vacuum hst_30min_delta  dry run
      vacuum hsy_30min_delta  dry run
      vacuum hum_30min_delta dry run
      vacuum iac_30min_delta  dry run
      vacuum ibm_30min_delta  dry run
      vacuum ice_30min_deltav dry run
      vacuum idxx_30min_delta  dry run
      vacuum iex_30min_delta  dry run
      vacuum iff_30min_delta  dry run
      vacuum igt_30min_delta  dry run
      vacuum ihrt_30min_delta  dry run
      vacuum ilmn_30min_delta dry run
      vacuum incy_30min_delta  dry run
      vacuum info_30min_delta  dry run
      vacuum infy_30min_delta dry run
      vacuum intc_30min_delta  dry run
      vacuum intu_30min_delta  dry run
      vacuum ip_30min_delta  dry run
      vacuum ipg_30min_delta dry run
      vacuum ipgp_30min_delta  dry run
      vacuum iqv_30min_delta  dry run
      vacuum ir_30min_delta  dry run
      vacuum irm_30min_delta dry run
      vacuum isrg_30min_delta dry run
      vacuum it_30min_delta  dry run
      vacuum itt_30min_delta  dry run
      vacuum itw_30min_delta  dry run
      vacuum ivz_30min_delta  dry run
      vacuum j_30min_delta  dry run
      vacuum jbht_30min_delta  dry run
      vacuum jbl_30min_delta  dry run
      vacuum jci_30min_delta dry run
      vacuum jd_30min_delta dry run
      vacuum jef_30min_delta  dry run
      vacuum jkhy_30min_delta  dry run
      vacuum jnj_30min_delta  dry run
      vacuum jnpr_30min_delta  dry run
      vacuum jp_30min_delta  dry run
      vacuum jpm_30min_delta  dry run
      vacuum jwn_30min_delta  dry run
      vacuum k_30min_delta dry run
      vacuum kbh_30min_delta  dry run
      vacuum key_30min_delta  dry run
      vacuum keys_30min_delta dry run
      vacuum khc_30min_delta  dry run
      vacuum kim_30min_delta  dry run
      vacuum klac_30min_delta dry run
      vacuum kmb_30min_delta  dry run
      vacuum kmi_30min_delta dry run
      vacuum kmx_30min_delta  dry run
      vacuum ko_30min_delta  dry run
      vacuum kodk_30min_delta  dry run
      vacuum kr_30min_delta  dry run
      vacuum kss_30min_delta  dry run
      vacuum ksu_30min_delta dry run
      vacuum l_30min_delta  dry run
      vacuum lbtyk_30min_delta  dry run
      vacuum ldos_30min_delta  dry run
      vacuum leg_30min_delta  dry run
      vacuum len_30min_delta  dry run
      vacuum lh_30min_delta  dry run
      vacuum lhx_30min_delta  dry run
      vacuum life_30min_delta  dry run
      vacuum lin_30min_delta  dry run
      vacuum lkq_30min_delta  dry run
      vacuum lly_30min_delta  dry run
      vacuum lmt_30min_delta  dry run
      vacuum lnc_30min_delta  dry run
      vacuum lnt_30min_delta  dry run
      vacuum logi_30min_delta  dry run
      vacuum low_30min_delta  dry run
      vacuum lrcx_30min_delta  dry run
      vacuum lsi_30min_delta  dry run
      vacuum lu_30min_delta dry run
      vacuum lumn_30min_delta dry run
      vacuum luv_30min_delta  dry run
      vacuum lvs_30min_delta  dry run
      vacuum lw_30min_delta  dry run
      vacuum lyb_30min_delta  dry run
      vacuum lyv_30min_delta  dry run
      vacuum m_30min_delta  dry run
      vacuum ma_30min_delta  dry run
      vacuum maa_30min_delta dry run
      vacuum mac_30min_delta  dry run
      vacuum mar_30min_delta dry run
      vacuum mas_30min_delta  dry run
      vacuum mat_30min_delta  dry run
      vacuum mbi_30min_delta  dry run
      vacuum mcd_30min_delta  dry run
      vacuum mchp_30min_delta dry run
      vacuum mck_30min_delta dry run
      vacuum mco_30min_delta  dry run
      vacuum mdlz_30min_delta  dry run
      vacuum mdp_30min_delta  dry run
      vacuum mdt_30min_delta  dry run
      vacuum met_30min_delta  dry run
      vacuum mgm_30min_delta  dry run
      vacuum mhk_30min_delta  dry run
      vacuum mkc_30min_delta  dry run
      vacuum mktx_30min_delta  dry run
      vacuum mlm_30min_delta  dry run
      vacuum mmc_30min_delta  dry run
      vacuum mmi_30min_delta  dry run
      vacuum mmm_30min_delta  dry run
      vacuum mnst_30min_delta  dry run
      vacuum mo_30min_delta  dry run
      vacuum moh_30min_delta  dry run
      vacuum mos_30min_delta  dry run
      vacuum mpc_30min_delta  dry run
      vacuum mpwr_30min_delta  dry run
      vacuum mrk_30min_delta  dry run
      vacuum mro_30min_delta  dry run
      vacuum mrvl_30min_delta  dry run
      vacuum ms_30min_delta  dry run
      vacuum msci_30min_delta  dry run
      vacuum msft_30min_delta  dry run
      vacuum msi_30min_delta  dry run
      vacuum mtb_30min_delta  dry run
      vacuum mtch_30min_delta  dry run
      vacuum mtd_30min_delta  dry run
      vacuum mtw_30min_delta  dry run
      vacuum mu_30min_delta  dry run
      vacuum mur_30min_delta  dry run
      vacuum navi_30min_delta  dry run
      vacuum nbr_30min_delta  dry run
      vacuum nclh_30min_delta  dry run
      vacuum ndaq_30min_delta  dry run
      vacuum ndsn_30min_delta  dry run
      vacuum ne_30min_delta  dry run
      vacuum nee_30min_delta  dry run
      vacuum nem_30min_delta  dry run
      vacuum nflx_30min_delta  dry run
      vacuum ni_30min_delta  dry run
      vacuum nke_30min_delta  dry run
      vacuum nktr_30min_delta dry run
      vacuum nlok_30min_delta  dry run
      vacuum nlsn_30min_delta  dry run
      vacuum noc_30min_delta  dry run
      vacuum nov_30min_delta dry run
      vacuum now_30min_delta  dry run
      vacuum nrg_30min_delta  dry run
      vacuum nsc_30min_delta  dry run
      vacuum ntap_30min_delta  dry run
      vacuum ntes_30min_delta  dry run
      vacuum ntrs_30min_delta  dry run
      vacuum nue_30min_delta  dry run
      vacuum nvda_30min_delta dry run
      vacuum nvr_30min_delta  dry run
      vacuum nwl_30min_delta  dry run
      vacuum nws_30min_delta  dry run
      vacuum nwsa_30min_delta  dry run
      vacuum nxpi_30min_delta  dry run
      vacuum nyt_30min_delta  dry run
      vacuum o_30min_delta  dry run
      vacuum odfl_30min_delta  dry run
      vacuum odp_30min_delta  dry run
      vacuum ogn_30min_delta dry run
      vacuum oi_30min_delta  dry run
      vacuum oke_30min_delta dry run
      vacuum omc_30min_delta  dry run
      vacuum one_30min_delta  dry run
      vacuum orcl_30min_delta  dry run
      vacuum orly_30min_delta  dry run
      vacuum otis_30min_delta dry run
      vacuum oxy_30min_delta  dry run
      vacuum par_30min_delta dry run
      vacuum payc_30min_delta  dry run
      vacuum payx_30min_delta dry run
      vacuum pbct_30min_delta  dry run
      vacuum pbi_30min_delta  dry run
      vacuum pcar_30min_delta  dry run
      vacuum pcg_30min_delta  dry run
      vacuum pdco_30min_delta  dry run
      vacuum peak_30min_delta dry run
      vacuum peg_30min_delta  dry run
      vacuum penn_30min_delta  dry run
      vacuum pep_30min_delta  dry run
      vacuum pfe_30min_delta dry run
      vacuum pfg_30min_delta  dry run
      vacuum pg_30min_delta  dry run
      vacuum pgr_30min_delta  dry run
      vacuum ph_30min_delta  dry run
      vacuum phm_30min_delta  dry run
      vacuum pkg_30min_delta  dry run
      vacuum pki_30min_delta  dry run
      vacuum pld_30min_delta dry run
      vacuum pll_30min_delta  dry run
      vacuum pm_30min_delta  dry run
      vacuum pnc_30min_delta  dry run
      vacuum pnr_30min_delta  dry run
      vacuum pnw_30min_delta  dry run
      vacuum pool_30min_delta  dry run
      vacuum ppg_30min_delta dry run
      vacuum ppl_30min_delta  dry run
      vacuum prgo_30min_delta dry run
      vacuum pri_30min_delta  dry run
      vacuum pru_30min_delta  dry run
      vacuum psa_30min_delta  dry run
      vacuum psx_30min_delta  dry run
      vacuum ptc_30min_delta  dry run
      vacuum pvh_30min_delta  dry run
      vacuum pwr_30min_delta  dry run
      vacuum pxd_30min_delta  dry run 
      vacuum pypl_30min_delta dry run
      vacuum qcom_30min_delta  dry run
      vacuum qgen_30min_delta  dry run
      vacuum qrvo_30min_delta  dry run
      vacuum r_30min_delta  dry run
      vacuum rcl_30min_delta  dry run
      vacuum re_30min_delta  dry run
      vacuum reg_30min_delta dry run
      vacuum regn_30min_delta  dry run
      vacuum rf_30min_delta dry run
      vacuum rhi_30min_delta  dry run
      vacuum rig_30min_delta dry run
      vacuum rjf_30min_delta  dry run
      vacuum rl_30min_delta  dry run
      vacuum rlgy_30min_delta  dry run
      vacuum rmd_30min_delta dry run
      vacuum rok_30min_delta  dry run
      vacuum rol_30min_delta  dry run
      vacuum rop_30min_delta  dry run
      vacuum rost_30min_delta  dry run
      vacuum rrc_30min_delta  dry run
      vacuum rrd_30min_delta  dry run
      vacuum rsg_30min_delta  dry run
      vacuum rtx_30min_delta  dry run
      vacuum ryaay_30min_delta  dry run
      vacuum s_30min_delta  dry run
      vacuum saic_30min_delta  dry run
      vacuum sanm_30min_delta  dry run
      vacuum sbac_30min_delta  dry run
      vacuum sbny_30min_delta dry run
      vacuum sbux_30min_delta  dry run
      vacuum schw_30min_delta  dry run
      vacuum se_30min_delta  dry run
      vacuum sedg_30min_delta  dry run
      vacuum see_30min_delta  dry run
      vacuum shw_30min_delta  dry run
      vacuum sig_30min_delta  dry run
      vacuum siri_30min_delta  dry run
      vacuum sitc_30min_delta  dry run
      vacuum sivb_30min_delta  dry run
      vacuum sjm_30min_delta   dry run
      vacuum slb_30min_delta  dry run
      vacuum slg_30min_delta  dry run
      vacuum slm_30min_delta  dry run
      vacuum sna_30min_delta  dry run
      vacuum snps_30min_delta  dry run
      vacuum so_30min_delta dry run
      vacuum spg_30min_delta  dry run
      vacuum spgi_30min_delta  dry run
      vacuum srcl_30min_delta  dry run
      vacuum sre_30min_delta  dry run
      vacuum ssp_30min_delta  dry run
      vacuum ste_30min_delta  dry run
      vacuum stt_30min_delta  dry run
      vacuum stx_30min_delta  dry run
      vacuum stz_30min_delta  dry run
      vacuum sun_30min_delta  dry run
      vacuum swk_30min_delta  dry run
      vacuum swks_30min_delta  dry run
      vacuum swn_30min_delta  dry run
      vacuum syf_30min_delta dry run
      vacuum syk_30min_delta  dry run
      vacuum syy_30min_delta  dry run
      vacuum t_30min_delta  dry run
      vacuum tap_30min_delta  dry run
      vacuum tdc_30min_delta  dry run
      vacuum tdg_30min_delta  dry run
      vacuum tdy_30min_delta  dry run
      vacuum tel_30min_delta  dry run
      vacuum ter_30min_delta  dry run
      vacuum teva_30min_delta  dry run
      vacuum tex_30min_delta  dry run
      vacuum tfc_30min_delta  dry run
      vacuum tfx_30min_delta  dry run
      vacuum tgna_30min_delta  dry run
      vacuum tgt_30min_delta  dry run
      vacuum thc_30min_delta  dry run
      vacuum tjx_30min_delta  dry run
      vacuum tmo_30min_delta  dry run
      vacuum tmus_30min_delta  dry run
      vacuum tpr_30min_delta  dry run
      vacuum trip_30min_delta  dry run
      vacuum trmb_30min_delta  dry run
      vacuum trow_30min_delta  dry run
      vacuum trv_30min_delta  dry run
      vacuum tsco_30min_delta  dry run
      vacuum tsla_30min_delta  dry run
      vacuum tsn_30min_delta  dry run
      vacuum ttwo_30min_delta dry run
      vacuum tup_30min_delta  dry run
      vacuum twtr_30min_delta  dry run
      vacuum txn_30min_delta  dry run
      vacuum txt_30min_delta dry run
      vacuum tyl_30min_delta  dry run
      vacuum ua_30min_delta  dry run
      vacuum uaa_30min_delta  dry run
      vacuum ual_30min_delta  dry run
      vacuum ucl_30min_delta  dry run
      vacuum udr_30min_delta  dry run
      vacuum uhs_30min_delta  dry run
      vacuum ulta_30min_delta  dry run
      vacuum unh_30min_delta  dry run
      vacuum unm_30min_delta  dry run
      vacuum unp_30min_delta  dry run
      vacuum upc_30min_delta  dry run
      vacuum ups_30min_delta  dry run
      vacuum urbn_30min_delta dry run
      vacuum uri_30min_delta  dry run
      vacuum usb_30min_delta  dry run
      vacuum v_30min_delta  dry run
      vacuum val_30min_delta dry run
      vacuum vfc_30min_delta  dry run
      vacuum viav_30min_delta dry run
      vacuum vlo_30min_delta  dry run
      vacuum vmc_30min_delta  dry run
      vacuum vno_30min_delta  dry run
      vacuum vnt_30min_delta  dry run
      vacuum vod_30min_delta  dry run
      vacuum vrsk_30min_delta  dry run
      vacuum vrsn_30min_delta  dry run
      vacuum vrts_30min_delta  dry run
      vacuum vrtx_30min_delta  dry run
      vacuum vtr_30min_delta  dry run
      vacuum vtrs_30min_delta  dry run
      vacuum vz_30min_delta  dry run
      vacuum wab_30min_delta  dry run
      vacuum wat_30min_delta  dry run
      vacuum wba_30min_delta  dry run
      vacuum wdc_30min_delta  dry run
      vacuum wec_30min_delta  dry run
      vacuum well_30min_delta  dry run
      vacuum wfc_30min_delta  dry run
      vacuum whr_30min_delta  dry run
      vacuum wltw_30min_delta  dry run
      vacuum wm_30min_delta  dry run
      vacuum wmb_30min_delta  dry run
      vacuum wmt_30min_delta  dry run
      vacuum wor_30min_delta  dry run
      vacuum wrb_30min_delta  dry run
      vacuum wrk_30min_delta  dry run
      vacuum wst_30min_delta  dry run
      vacuum wu_30min_delta  dry run
      vacuum wy_30min_delta  dry run
      vacuum wynn_30min_delta dry run
      vacuum x_30min_delta dry run
      vacuum xel_30min_delta dry run
      vacuum xlnx_30min_delta dry run
      vacuum xom_30min_delta dry run
      vacuum xray_30min_delta dry run
      vacuum xrx_30min_delta dry run
      vacuum xyl_30min_delta dry run
      vacuum yum_30min_delta dry run
      vacuum zbh_30min_delta dry run
      vacuum zbra_30min_delta dry run
      vacuum zion_30min_delta dry run
      vacuum zts_30min_delta dry run

# COMMAND ----------

%sql
describe history aapl_30min_delta 

# COMMAND ----------

%sql
-- Use this when we need to manually vacuum
--set spark.databricks.delta.retentionDurationCheck.enabled = False

-- Use this when we don't need to manually vacuum
set spark.databricks.delta.retentionDurationCheck.enabled = True
