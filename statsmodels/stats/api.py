# pylint: disable=W0611
# flake8: noqa

from . import diagnostic
from .diagnostic import (
    acorr_ljungbox, acorr_breusch_godfrey, acorr_lm,
    compare_cox, compare_j, compare_encompassing,
    het_goldfeldquandt,
    het_breuschpagan, het_white, het_arch,
    linear_harvey_collier, linear_rainbow, linear_lm, linear_reset,
    breaks_cusumolsresid, breaks_hansen, recursive_olsresiduals,
    spec_white
    )
from ._adnorm import normal_ad
from ._lilliefors import lilliefors

from ._knockoff import RegressionFDR
from . import multicomp
from .multitest import (multipletests, fdrcorrection, fdrcorrection_twostage,
                        local_fdr, NullDistribution)
from .multicomp import tukeyhsd
from . import gof
from .gof import (powerdiscrepancy, gof_chisquare_discrete,
                  chisquare_effectsize)
from . import stattools
from .stattools import durbin_watson, omni_normtest, jarque_bera

from . import sandwich_covariance
from .sandwich_covariance import (
    cov_cluster, cov_cluster_2groups, cov_nw_panel,
    cov_hac, cov_white_simple,
    cov_hc0, cov_hc1, cov_hc2, cov_hc3,
    se_cov
    )

from .weightstats import (DescrStatsW, CompareMeans, ttest_ind, ttost_ind,
                          ttost_paired, ztest, ztost, zconfint)

from .proportion import (
    binom_test_reject_interval, binom_test,
    binom_tost, binom_tost_reject_interval,
    power_binom_tost, power_ztost_prop,
    proportion_confint, proportion_effectsize,
    samplesize_confint_proportion,
    proportions_chisquare, proportions_chisquare_allpairs,
    proportions_chisquare_pairscontrol, proportions_ztest,
    proportions_ztost, multinomial_proportions_confint,
    # 2 sample functions:
    confint_proportions_2indep, power_proportions_2indep,
    samplesize_proportions_2indep_onetail,
    test_proportions_2indep, tost_proportions_2indep,
    )

from .rates import (
    etest_poisson_2indep, test_poisson_2indep, tost_poisson_2indep,
    )

from .oneway import (
        # mean and scale
        anova_oneway, equivalence_oneway,
        test_scale_oneway, equivalence_scale_oneway,
        # power
        effectsize_oneway,
        power_equivalence_oneway, simulate_power_equivalence_oneway,
        # from stats
        anova_generic, equivalence_oneway_generic,
        # effect size
        confint_effectsize_oneway, confint_noncentrality,
        convert_effectsize_fsqu,
        f2_to_wellek, fstat_to_wellek, wellek_to_f2
        )

from .multivariate import (
        test_cov, test_cov_blockdiagonal, test_cov_diagonal, test_cov_oneway,
        test_cov_spherical,
        test_mvmean, confint_mvmean, confint_mvmean_fromstats,
        test_mvmean_2indep,
        )

from .power import (TTestPower, TTestIndPower, GofChisquarePower,
                    NormalIndPower, FTestAnovaPower, FTestPower,
                    tt_solve_power, tt_ind_solve_power, zt_ind_solve_power)

from .descriptivestats import Describe

from .anova import anova_lm, AnovaRM

from .inter_rater import (
    cohens_kappa, fleiss_kappa
    )

from .oaxaca import OaxacaBlinder

from . import moment_helpers
from .correlation_tools import (
    corr_clipped, corr_nearest,
    corr_nearest_factor, corr_thresholded, cov_nearest,
    cov_nearest_factor_homog, FactoredPSDMatrix)

from statsmodels.sandbox.stats.runs import Runs, runstest_1samp, runstest_2samp

from statsmodels.stats.contingency_tables import (mcnemar, cochrans_q,
                                                  SquareTable,
                                                  Table2x2,
                                                  Table,
                                                  StratifiedTable)
from .mediation import Mediation

from .meta_analysis import (
    combine_effects, effectsize_2proportions, effectsize_smd,
    )

__all__ = ["acorr_lm", "acorr_breusch_godfrey", "acorr_ljungbox", "anova_lm",
           "AnovaRM", "binom_test",
           "binom_test_reject_interval", "Mediation", "mcnemar", "cochrans_q", "SquareTable",
           "Table", 'Table2x2', "StratifiedTable", "corr_clipped", "corr_nearest",
           "corr_nearest_factor", "corr_thresholded", "cov_nearest", "cov_nearest_factor_homog",
           "FactoredPSDMatrix", "Describe", "OaxacaBlinder", "Runs", "runstest_1samp",
           "runstest_2samp", "moment_helpers", "binom_tost", "binom_tost_reject_interval",
           "power_binom_tost", "power_ztost_prop", "proportion_confint", "proportion_effectsize",
           "proportions_chisquare", "proportions_chisquare_allpairs",
           "proportions_chisquare_pairscontrol", "proportions_ztest", "proportions_ztost",
           "samplesize_confint_proportion",
           "confint_proportions_2indep", "power_proportions_2indep",
           "samplesize_proportions_2indep_onetail",
           "test_proportions_2indep", "tost_proportions_2indep",
           "multinomial_proportions_confint",
           "TTestPower", "TTestIndPower", "GofChisquarePower",
           "NormalIndPower", "FTestAnovaPower", "FTestPower", "tt_solve_power",
           "tt_ind_solve_power", "zt_ind_solve_power", "cov_cluster", "cov_cluster_2groups",
           "cov_nw_panel", "cov_hac", "cov_white_simple", "cov_hc0", "cov_hc1", "cov_hc2",
           "cov_hc3", "se_cov", "compare_cox", "compare_j",
           "compare_encompassing", "het_goldfeldquandt", "het_breuschpagan",
           "het_white", "het_arch", "linear_harvey_collier", "linear_rainbow", "linear_lm",
           "linear_reset", "breaks_cusumolsresid", "breaks_hansen", "recursive_olsresiduals",
           "spec_white", "diagnostic", "normal_ad", "lilliefors", "RegressionFDR", "multicomp",
           "multipletests", "fdrcorrection", "fdrcorrection_twostage", "local_fdr",
           "NullDistribution", "tukeyhsd", "gof", "powerdiscrepancy", "gof_chisquare_discrete",
           "chisquare_effectsize", "stattools", "durbin_watson", "omni_normtest", "jarque_bera",
           "sandwich_covariance", "DescrStatsW", "CompareMeans", "ttest_ind", "ttost_ind",
           "ttost_paired", "ztest", "ztost", "zconfint",
           "etest_poisson_2indep", "test_poisson_2indep", "tost_poisson_2indep",
           "combine_effects", "effectsize_2proportions", "effectsize_smd",
           "cohens_kappa", "fleiss_kappa",
           "anova_oneway", "equivalence_oneway", "test_scale_oneway",
           "equivalence_scale_oneway", "effectsize_oneway",
           "power_equivalence_oneway", "simulate_power_equivalence_oneway",
           "anova_generic", "equivalence_oneway_generic",
           "confint_effectsize_oneway", "confint_noncentrality",
           "convert_effectsize_fsqu", "f2_to_wellek", "fstat_to_wellek",
           "wellek_to_f2",
           "test_cov", "test_cov_blockdiagonal", "test_cov_diagonal",
           "test_cov_oneway", "test_cov_spherical", "test_mvmean",
           "confint_mvmean", "confint_mvmean_fromstats", "test_mvmean_2indep",
           ]
