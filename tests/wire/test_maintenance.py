from .conftest import get_client, verify_request_count


def test_maintenance_get_defect_types() -> None:
    """Test getDefectTypes endpoint with WireMock"""
    test_id = "maintenance.get_defect_types.0"
    client = get_client(test_id)
    client.maintenance.get_defect_types()
    verify_request_count(test_id, "GET", "/defect-types", None, 1)


def test_maintenance_stream_defects() -> None:
    """Test streamDefects endpoint with WireMock"""
    test_id = "maintenance.stream_defects.0"
    client = get_client(test_id)
    client.maintenance.stream_defects(start_time="startTime")
    verify_request_count(test_id, "GET", "/defects/stream", {"startTime": "startTime"}, 1)


def test_maintenance_get_defect() -> None:
    """Test getDefect endpoint with WireMock"""
    test_id = "maintenance.get_defect.0"
    client = get_client(test_id)
    client.maintenance.get_defect(id="id")
    verify_request_count(test_id, "GET", "/defects/id", None, 1)


def test_maintenance_get_dvirs() -> None:
    """Test getDvirs endpoint with WireMock"""
    test_id = "maintenance.get_dvirs.0"
    client = get_client(test_id)
    client.maintenance.get_dvirs(start_time="startTime")
    verify_request_count(test_id, "GET", "/dvirs/stream", {"startTime": "startTime"}, 1)


def test_maintenance_get_dvir() -> None:
    """Test getDvir endpoint with WireMock"""
    test_id = "maintenance.get_dvir.0"
    client = get_client(test_id)
    client.maintenance.get_dvir(id="id")
    verify_request_count(test_id, "GET", "/dvirs/id", None, 1)


def test_maintenance_update_dvir_defect() -> None:
    """Test updateDvirDefect endpoint with WireMock"""
    test_id = "maintenance.update_dvir_defect.0"
    client = get_client(test_id)
    client.maintenance.update_dvir_defect(id="id")
    verify_request_count(test_id, "PATCH", "/fleet/defects/id", None, 1)


def test_maintenance_create_dvir() -> None:
    """Test createDvir endpoint with WireMock"""
    test_id = "maintenance.create_dvir.0"
    client = get_client(test_id)
    client.maintenance.create_dvir(author_id="11", safety_status="safe", type="mechanic")
    verify_request_count(test_id, "POST", "/fleet/dvirs", None, 1)


def test_maintenance_update_dvir() -> None:
    """Test updateDvir endpoint with WireMock"""
    test_id = "maintenance.update_dvir.0"
    client = get_client(test_id)
    client.maintenance.update_dvir(id="id", author_id="11", is_resolved=True)
    verify_request_count(test_id, "PATCH", "/fleet/dvirs/id", None, 1)


def test_maintenance_list_vendor_categories() -> None:
    """Test listVendorCategories endpoint with WireMock"""
    test_id = "maintenance.list_vendor_categories.0"
    client = get_client(test_id)
    client.maintenance.list_vendor_categories()
    verify_request_count(test_id, "GET", "/fleet/maintenance/vendor-categories", None, 1)


def test_maintenance_list_vendor_locations() -> None:
    """Test listVendorLocations endpoint with WireMock"""
    test_id = "maintenance.list_vendor_locations.0"
    client = get_client(test_id)
    client.maintenance.list_vendor_locations()
    verify_request_count(test_id, "GET", "/fleet/maintenance/vendor-locations", None, 1)


def test_maintenance_create_vendor_location() -> None:
    """Test createVendorLocation endpoint with WireMock"""
    test_id = "maintenance.create_vendor_location.0"
    client = get_client(test_id)
    client.maintenance.create_vendor_location(address_id="281474976710656")
    verify_request_count(test_id, "POST", "/fleet/maintenance/vendor-locations", None, 1)


def test_maintenance_delete_vendor_location() -> None:
    """Test deleteVendorLocation endpoint with WireMock"""
    test_id = "maintenance.delete_vendor_location.0"
    client = get_client(test_id)
    client.maintenance.delete_vendor_location(id="id")
    verify_request_count(test_id, "DELETE", "/fleet/maintenance/vendor-locations", {"id": "id"}, 1)


def test_maintenance_update_vendor_location() -> None:
    """Test updateVendorLocation endpoint with WireMock"""
    test_id = "maintenance.update_vendor_location.0"
    client = get_client(test_id)
    client.maintenance.update_vendor_location(id="id")
    verify_request_count(test_id, "PATCH", "/fleet/maintenance/vendor-locations", {"id": "id"}, 1)


def test_maintenance_list_vendors() -> None:
    """Test listVendors endpoint with WireMock"""
    test_id = "maintenance.list_vendors.0"
    client = get_client(test_id)
    client.maintenance.list_vendors()
    verify_request_count(test_id, "GET", "/fleet/maintenance/vendors", None, 1)


def test_maintenance_create_vendor() -> None:
    """Test createVendor endpoint with WireMock"""
    test_id = "maintenance.create_vendor.0"
    client = get_client(test_id)
    client.maintenance.create_vendor(name="12345")
    verify_request_count(test_id, "POST", "/fleet/maintenance/vendors", None, 1)


def test_maintenance_delete_vendor() -> None:
    """Test deleteVendor endpoint with WireMock"""
    test_id = "maintenance.delete_vendor.0"
    client = get_client(test_id)
    client.maintenance.delete_vendor(id="id")
    verify_request_count(test_id, "DELETE", "/fleet/maintenance/vendors", {"id": "id"}, 1)


def test_maintenance_update_vendor() -> None:
    """Test updateVendor endpoint with WireMock"""
    test_id = "maintenance.update_vendor.0"
    client = get_client(test_id)
    client.maintenance.update_vendor(id="id")
    verify_request_count(test_id, "PATCH", "/fleet/maintenance/vendors", {"id": "id"}, 1)


def test_maintenance_list_parts() -> None:
    """Test listParts endpoint with WireMock"""
    test_id = "maintenance.list_parts.0"
    client = get_client(test_id)
    client.maintenance.list_parts()
    verify_request_count(test_id, "GET", "/maintenance/parts", None, 1)


def test_maintenance_create_part() -> None:
    """Test createPart endpoint with WireMock"""
    test_id = "maintenance.create_part.0"
    client = get_client(test_id)
    client.maintenance.create_part(part_number="12345")
    verify_request_count(test_id, "POST", "/maintenance/parts", None, 1)


def test_maintenance_delete_part() -> None:
    """Test deletePart endpoint with WireMock"""
    test_id = "maintenance.delete_part.0"
    client = get_client(test_id)
    client.maintenance.delete_part(id="id")
    verify_request_count(test_id, "DELETE", "/maintenance/parts", {"id": "id"}, 1)


def test_maintenance_update_part() -> None:
    """Test updatePart endpoint with WireMock"""
    test_id = "maintenance.update_part.0"
    client = get_client(test_id)
    client.maintenance.update_part(id="id")
    verify_request_count(test_id, "PATCH", "/maintenance/parts", {"id": "id"}, 1)


def test_maintenance_list_part_inventory() -> None:
    """Test listPartInventory endpoint with WireMock"""
    test_id = "maintenance.list_part_inventory.0"
    client = get_client(test_id)
    client.maintenance.list_part_inventory()
    verify_request_count(test_id, "GET", "/maintenance/parts/inventory-location", None, 1)


def test_maintenance_create_part_inventory_location() -> None:
    """Test createPartInventoryLocation endpoint with WireMock"""
    test_id = "maintenance.create_part_inventory_location.0"
    client = get_client(test_id)
    client.maintenance.create_part_inventory_location()
    verify_request_count(test_id, "POST", "/maintenance/parts/inventory-location", None, 1)


def test_maintenance_update_part_inventory_location() -> None:
    """Test updatePartInventoryLocation endpoint with WireMock"""
    test_id = "maintenance.update_part_inventory_location.0"
    client = get_client(test_id)
    client.maintenance.update_part_inventory_location()
    verify_request_count(test_id, "PATCH", "/maintenance/parts/inventory-location", None, 1)


def test_maintenance_create_stock_movement() -> None:
    """Test createStockMovement endpoint with WireMock"""
    test_id = "maintenance.create_stock_movement.0"
    client = get_client(test_id)
    client.maintenance.create_stock_movement(movement_type="12345", part_samsara_id="12345", quantity=123.45)
    verify_request_count(test_id, "POST", "/maintenance/parts/stock-movements", None, 1)


def test_maintenance_list_part_transactions() -> None:
    """Test listPartTransactions endpoint with WireMock"""
    test_id = "maintenance.list_part_transactions.0"
    client = get_client(test_id)
    client.maintenance.list_part_transactions(happened_at_time_start="happenedAtTimeStart")
    verify_request_count(
        test_id, "GET", "/maintenance/parts/transactions", {"happenedAtTimeStart": "happenedAtTimeStart"}, 1
    )


def test_maintenance_list_purchase_orders() -> None:
    """Test listPurchaseOrders endpoint with WireMock"""
    test_id = "maintenance.list_purchase_orders.0"
    client = get_client(test_id)
    client.maintenance.list_purchase_orders(
        ids="281474976710656",
        po_numbers="PO-1001",
        vendor_ids="281474976710656",
        end_time="2026-07-31T00:00:00Z",
        start_time="2026-07-01T00:00:00Z",
    )
    verify_request_count(
        test_id,
        "GET",
        "/maintenance/purchase-orders",
        {
            "ids": "281474976710656",
            "poNumbers": "PO-1001",
            "vendorIds": "281474976710656",
            "endTime": "2026-07-31T00:00:00Z",
            "startTime": "2026-07-01T00:00:00Z",
        },
        1,
    )


def test_maintenance_create_purchase_order() -> None:
    """Test createPurchaseOrder endpoint with WireMock"""
    test_id = "maintenance.create_purchase_order.0"
    client = get_client(test_id)
    client.maintenance.create_purchase_order(order_status="Unknown", vendor_id="281474976710656")
    verify_request_count(test_id, "POST", "/maintenance/purchase-orders", None, 1)


def test_maintenance_delete_purchase_order() -> None:
    """Test deletePurchaseOrder endpoint with WireMock"""
    test_id = "maintenance.delete_purchase_order.0"
    client = get_client(test_id)
    client.maintenance.delete_purchase_order(id="id")
    verify_request_count(test_id, "DELETE", "/maintenance/purchase-orders", {"id": "id"}, 1)


def test_maintenance_update_purchase_order() -> None:
    """Test updatePurchaseOrder endpoint with WireMock"""
    test_id = "maintenance.update_purchase_order.0"
    client = get_client(test_id)
    client.maintenance.update_purchase_order(id="id")
    verify_request_count(test_id, "PATCH", "/maintenance/purchase-orders", {"id": "id"}, 1)


def test_maintenance_list_time_entries() -> None:
    """Test listTimeEntries endpoint with WireMock"""
    test_id = "maintenance.list_time_entries.0"
    client = get_client(test_id)
    client.maintenance.list_time_entries(start_time="startTime")
    verify_request_count(test_id, "GET", "/maintenance/time-entries/stream", {"startTime": "startTime"}, 1)


def test_maintenance_list_warranties() -> None:
    """Test listWarranties endpoint with WireMock"""
    test_id = "maintenance.list_warranties.0"
    client = get_client(test_id)
    client.maintenance.list_warranties()
    verify_request_count(test_id, "GET", "/maintenance/warranties", None, 1)


def test_maintenance_create_warranty() -> None:
    """Test createWarranty endpoint with WireMock"""
    test_id = "maintenance.create_warranty.0"
    client = get_client(test_id)
    client.maintenance.create_warranty(name="12345")
    verify_request_count(test_id, "POST", "/maintenance/warranties", None, 1)


def test_maintenance_delete_warranty() -> None:
    """Test deleteWarranty endpoint with WireMock"""
    test_id = "maintenance.delete_warranty.0"
    client = get_client(test_id)
    client.maintenance.delete_warranty(id="id")
    verify_request_count(test_id, "DELETE", "/maintenance/warranties", {"id": "id"}, 1)


def test_maintenance_update_warranty() -> None:
    """Test updateWarranty endpoint with WireMock"""
    test_id = "maintenance.update_warranty.0"
    client = get_client(test_id)
    client.maintenance.update_warranty(id="id")
    verify_request_count(test_id, "PATCH", "/maintenance/warranties", {"id": "id"}, 1)


def test_maintenance_list_warranty_asset_assignments() -> None:
    """Test listWarrantyAssetAssignments endpoint with WireMock"""
    test_id = "maintenance.list_warranty_asset_assignments.0"
    client = get_client(test_id)
    client.maintenance.list_warranty_asset_assignments(warranty_id="warrantyId")
    verify_request_count(test_id, "GET", "/maintenance/warranties/assets", {"warrantyId": "warrantyId"}, 1)


def test_maintenance_replace_warranty_asset_assignments() -> None:
    """Test replaceWarrantyAssetAssignments endpoint with WireMock"""
    test_id = "maintenance.replace_warranty_asset_assignments.0"
    client = get_client(test_id)
    client.maintenance.replace_warranty_asset_assignments()
    verify_request_count(test_id, "POST", "/maintenance/warranties/assets/replace", None, 1)


def test_maintenance_list_warranty_claims() -> None:
    """Test listWarrantyClaims endpoint with WireMock"""
    test_id = "maintenance.list_warranty_claims.0"
    client = get_client(test_id)
    client.maintenance.list_warranty_claims()
    verify_request_count(test_id, "GET", "/maintenance/warranty-claims", None, 1)


def test_maintenance_create_warranty_claim() -> None:
    """Test createWarrantyClaim endpoint with WireMock"""
    test_id = "maintenance.create_warranty_claim.0"
    client = get_client(test_id)
    client.maintenance.create_warranty_claim(asset_id="281474976710656")
    verify_request_count(test_id, "POST", "/maintenance/warranty-claims", None, 1)


def test_maintenance_delete_warranty_claim() -> None:
    """Test deleteWarrantyClaim endpoint with WireMock"""
    test_id = "maintenance.delete_warranty_claim.0"
    client = get_client(test_id)
    client.maintenance.delete_warranty_claim(id="id")
    verify_request_count(test_id, "DELETE", "/maintenance/warranty-claims", {"id": "id"}, 1)


def test_maintenance_update_warranty_claim() -> None:
    """Test updateWarrantyClaim endpoint with WireMock"""
    test_id = "maintenance.update_warranty_claim.0"
    client = get_client(test_id)
    client.maintenance.update_warranty_claim(id="id")
    verify_request_count(test_id, "PATCH", "/maintenance/warranty-claims", {"id": "id"}, 1)


def test_maintenance_v_1_get_fleet_maintenance_list() -> None:
    """Test V1getFleetMaintenanceList endpoint with WireMock"""
    test_id = "maintenance.v_1_get_fleet_maintenance_list.0"
    client = get_client(test_id)
    client.maintenance.v_1_get_fleet_maintenance_list()
    verify_request_count(test_id, "GET", "/v1/fleet/maintenance/list", None, 1)
