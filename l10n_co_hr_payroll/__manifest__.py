# -*- coding: utf-8 -*-
# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name":
    "Nomina Localizacion Colombiana",
    "version":
    "12.0",
    "author":
    "EXA Auto Parts Github@exaap, Alejandro Olano Github@alejo-code",
    "category":
    "Generic Modules/Human Resources",
    "depends": [
        "hr", "hr_contract", "hr_holidays", "hr_payroll", "hr_payroll_account",
        "account_fiscal_year"
    ],
    "description":
    """
Modulo de nomina para la localizacion colombiana
    """,
    "data": [
        "views/res_config_settings_view.xml",
        "views/hr_salary_rule_view.xml",
        "views/hr_contract_view.xml",
        "views/hr_payslip_view.xml",
        "views/hr_novedades_view.xml",
        "views/hr_leave_view.xml",
        "security/ir.model.access.csv",
    ]
}