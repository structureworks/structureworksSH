# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

from odoo import models, _


class ReportBomStructure(models.AbstractModel):
    _inherit = 'report.mrp.report_bom_structure'

    def _get_pdf_line(self, bom_id, product_id=False, qty=1, child_bom_ids=[], unfolded=False):
        data = super(ReportBomStructure, self)._get_pdf_line(bom_id, product_id, qty, child_bom_ids, unfolded)
        for line in data.get('lines'):
            if line.get('prod_id') and line.get('type') and line.get('type') == 'bom':
                line.update({'product': self.env['product.product'].browse(line.get('prod_id'))})
        return data

    def _get_bom(self, bom_id=False, product_id=False, line_qty=False, line_id=False, level=False):
        lines = super(ReportBomStructure, self)._get_bom(bom_id, product_id, line_qty, line_id, level)
        total_weight = 0
        total_volume = 0
        if lines.get('components'):
            for component in lines.get('components'):
                if component.get('prod_id'):
                    product_id = self.env['product.product'].browse(component.get('prod_id'))
                    component.update({'product': product_id})
                    total_weight += product_id.weight * component.get('prod_qty')
                    total_volume += product_id.volume * component.get('prod_qty')
            lines.update({'total_weight': round(total_weight, 2), 'total_volume': round(total_volume, 2)})
            # lines.update({'total_weight': total_weight, 'total_volume': total_volume})
        return lines
