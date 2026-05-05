"""
Simple ETL Pipeline for Jenkins CI/CD Demo
Extracts sample data, transforms it, and loads to output file
"""
import pandas as pd
import json
from datetime import datetime

def extract():
    """Extract: Generate sample sales data"""
    print("📥 EXTRACT: Generating sample data...")
    data = {
        'transaction_id': [1001, 1002, 1003, 1004, 1005],
        'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop'],
        'amount': [1200, 25, 75, 300, 1100],
        'date': ['2026-05-01', '2026-05-02', '2026-05-02', '2026-05-03', '2026-05-04']
    }
    df = pd.DataFrame(data)
    print(f"✅ Extracted {len(df)} records")
    return df

def transform(df):
    """Transform: Add calculated fields and clean data"""
    print("🔄 TRANSFORM: Processing data...")
    
    # Add tax calculation (10%)
    df['tax'] = df['amount'] * 0.10
    df['total'] = df['amount'] + df['tax']
    
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Add category
    df['category'] = df['product'].apply(lambda x: 'Hardware' if x in ['Laptop', 'Monitor'] else 'Accessories')
    
    print(f"✅ Transformed {len(df)} records")
    return df

def load(df, output_file='output/sales_report.csv'):
    """Load: Save transformed data"""
    print(f"💾 LOAD: Saving to {output_file}...")
    
    # Create output directory if it doesn't exist
    import os
    os.makedirs('output', exist_ok=True)
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    
    # Save metadata
    metadata = {
        'timestamp': datetime.now().isoformat(),
        'records_processed': len(df),
        'total_revenue': float(df['total'].sum()),
        'status': 'SUCCESS'
    }
    
    with open('output/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"✅ Loaded {len(df)} records successfully")
    print(f"📊 Total Revenue: ${metadata['total_revenue']:.2f}")
    return metadata

def run_pipeline():
    """Main pipeline execution"""
    print("\n" + "="*50)
    print("🚀 Starting ETL Pipeline")
    print("="*50 + "\n")
    
    try:
        # ETL Steps
        raw_data = extract()
        transformed_data = transform(raw_data)
        metadata = load(transformed_data)
        
        print("\n" + "="*50)
        print("✅ Pipeline completed successfully!")
        print("="*50 + "\n")
        return 0
        
    except Exception as e:
        print(f"\n❌ ERROR: Pipeline failed - {str(e)}\n")
        return 1

if __name__ == "__main__":
    exit(run_pipeline())
