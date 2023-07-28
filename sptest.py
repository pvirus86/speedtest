# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 14:40:06 2023

@author: Pulkit
"""
import speedtest

def test_speed():
    st = speedtest.Speedtest()
    
    # Test download speed
    st.download(threads=None)
    download_speed = st.results.download / (1024 * 1024)  # Convert to Mbps
    print(f"Download Speed: {download_speed:.2f} Mbps")
    
    # Test upload speed
    st.upload(threads=None)
    upload_speed = st.results.upload / (1024 * 1024)  # Convert to Mbps
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    test_speed()
