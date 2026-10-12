`timescale 1ns / 1ps

module Array2_Detector_tb;

    // 1. Testbench sinyal tanımları (Verilog'da reg ve wire kullanılır)
    reg clk;
    reg rst;
    reg in;
    wire seq_a_detected;
    wire seq_b_detected;

    // 2. Test edilecek modülü (DUT) bağlama (Instantiation)
    Array2_Detector uut (
        .clk(clk),
        .rst(rst),
        .in(in),
        .seq_a_detected(seq_a_detected),
        .seq_b_detected(seq_b_detected)
    );

    // 3. Saat (Clock) Sinyali Üretimi (Periyot = 10ns)
    always #5 clk = ~clk;

    // 4. Test Senaryoları
    initial begin
        // Başlangıç değerleri
        clk = 1'b0;
        rst = 1'b1;
        in  = 1'b0;

        // 20ns sonra reset'i kaldır
        #20;
        rst = 1'b0;
        
        // --- SENARYO 1: Dizi A'yı test et ("1101") ---
        #10 in = 1'b1; // 1. adım
        #10 in = 1'b1; // 2. adım
        #10 in = 1'b0; // 3. adım
        #10 in = 1'b1; // 4. adım -> seq_a_detected 1 olmalı!

        #10 in = 1'b0; 
        #10 in = 1'b0;

        // --- SENARYO 2: Dizi B'yi test et ("1011") ---
        #10 in = 1'b1; // 1. adım
        #10 in = 1'b0; // 2. adım
        #10 in = 1'b1; // 3. adım
        #10 in = 1'b1; // 4. adım -> seq_b_detected 1 olmalı!

        // --- SENARYO 3: Karışık Akış ---
        #10 in = 1'b0;
        #10 in = 1'b1;
        #10 in = 1'b1;
        #10 in = 1'b1;
        #10 in = 1'b0;

        // Simülasyonu bitir
        #50;
        $finish;
    end

    // 5. Konsol Takip Ekranı ($monitor)
    initial begin
        $monitor("Zaman = %0t ns | rst = %b | in = %b || Seq_A_Det = %b | Seq_B_Det = %b", 
                 $time, rst, in, seq_a_detected, seq_b_detected);
    end

endmodule