"""
Data Quality Tests for ETL Pipeline
Validates output data integrity and business rules
"""
import pandas as pd
import json
import os
import sys

def test_output_files_exist():
    """Test 1: Verify output files are created"""
    print("🧪 Test 1: Checking if output files exist...")
    
    required_files = ['output/sales_report.csv', 'output/metadata.json']
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"   ❌ FAIL: {file} not found")
            return False
        print(f"   ✅ PASS: {file} exists")
    
    return True

def test_data_quality():
    """Test 2: Validate data quality and business rules"""
    print("🧪 Test 2: Validating data quality...")
    
    df = pd.read_csv('output/sales_report.csv')
    
    # Check row count
    if len(df) < 1:
        print("   ❌ FAIL: No data in output")
        return False
    print(f"   ✅ PASS: Found {len(df)} records")
    
    # Check required columns
    required_cols = ['transaction_id', 'product', 'amount', 'tax', 'total', 'category']
    for col in required_cols:
        if col not in df.columns:
            print(f"   ❌ FAIL: Missing column '{col}'")
            return False
    print(f"   ✅ PASS: All required columns present")
    
    # Check no null values in critical columns
    if df[['transaction_id', 'amount', 'total']].isnull().any().any():
        print("   ❌ FAIL: Found null values in critical columns")
        return False
    print("   ✅ PASS: No null values in critical columns")
    
    # Validate tax calculation (10%)
    df['expected_tax'] = df['amount'] * 0.10
    if not (df['tax'].round(2) == df['expected_tax'].round(2)).all():
        print("   ❌ FAIL: Tax calculation is incorrect")
        return False
    print("   ✅ PASS: Tax calculation is correct (10%)")
    
    # Validate total = amount + tax
    df['expected_total'] = df['amount'] + df['tax']
    if not (df['total'].round(2) == df['expected_total'].round(2)).all():
        print("   ❌ FAIL: Total calculation is incorrect")
        return False
    print("   ✅ PASS: Total calculation is correct")
    
    return True

def test_metadata():
    """Test 3: Verify metadata correctness"""
    print("🧪 Test 3: Checking metadata...")
    
    with open('output/metadata.json', 'r') as f:
        metadata = json.load(f)
    
    # Check required fields
    required_fields = ['timestamp', 'records_processed', 'total_revenue', 'status']
    for field in required_fields:
        if field not in metadata:
            print(f"   ❌ FAIL: Missing metadata field '{field}'")
            return False
    print("   ✅ PASS: All metadata fields present")
    
    # Check status
    if metadata['status'] != 'SUCCESS':
        print(f"   ❌ FAIL: Status is '{metadata['status']}', expected 'SUCCESS'")
        return False
    print("   ✅ PASS: Pipeline status is SUCCESS")
    
    # Verify record count matches
    df = pd.read_csv('output/sales_report.csv')
    if metadata['records_processed'] != len(df):
        print(f"   ❌ FAIL: Metadata count ({metadata['records_processed']}) doesn't match actual ({len(df)})")
        return False
    print(f"   ✅ PASS: Record count matches ({metadata['records_processed']})")
    
    return True

def run_all_tests():
    """Execute all test suites"""
    print("\n" + "="*50)
    print("🧪 Running Data Quality Tests")
    print("="*50 + "\n")
    
    tests = [
        test_output_files_exist,
        test_data_quality,
        test_metadata
    ]
    
    results = []
    for test in tests:
        result = test()
        results.append(result)
        print()
    
    # Summary
    print("="*50)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✅ ALL TESTS PASSED ({passed}/{total})")
        print("="*50 + "\n")
        return 0
    else:
        print(f"❌ TESTS FAILED ({passed}/{total} passed)")
        print("="*50 + "\n")
        return 1

if __name__ == "__main__":
    exit(run_all_tests())
