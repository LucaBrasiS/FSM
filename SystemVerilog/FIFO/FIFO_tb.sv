`timescale 1ns / 1ps

module FIFO_tb;

    logic       clk;
    logic       rst;
    logic       wr_en;
    logic       rd_en;
    logic [7:0] din;
    logic [7:0] dout;
    logic       empty;
    logic       full;

    // Test edilecek modül (DUT)
    FIFO uut (
        .clk(clk),
        .rst(rst),
        .wr_en(wr_en),
        .rd_en(rd_en),
        .din(din),
        .dout(dout),
        .empty(empty),
        .full(full)
    );

    // Saat Sinyali Üretimi (10ns periyot)
    always #5 clk = ~clk;

    initial begin
        clk   = 0;
        rst   = 1;
        wr_en = 0;
        rd_en = 0;
        din   = 8'h00;

        #20;
        rst = 0; // Reset kaldırıldı

        // --- SENARYO 1: Kuyruğa Veri Yazma (Write) ---
        @(posedge clk);
        wr_en = 1; din = 8'hAA;
        @(posedge clk);
        din = 8'hBB;
        @(posedge clk);
        din = 8'hCC;
        @(posedge clk);
        wr_en = 0; // Yazmayı durdur

        #20;

        // --- SENARYO 2: Kuyruktan Veri Okuma (Read) ---
        @(posedge clk);
        rd_en = 1;
        @(posedge clk);
        @(posedge clk);
        @(posedge clk);
        rd_en = 0; // Okumayı durdur

        #40;
        $finish;
    end

    initial begin
        $monitor("Zaman = %0t ns | wr = %b | rd = %b | din = %h | dout = %h | empty = %b | full = %b", 
                 $time, wr_en, rd_en, din, dout, empty, full);
    end

endmodule