`timescale 1ns / 1ps

module FIFO_tb;

    reg       clk;
    reg       rst;
    reg       wr_en;
    reg       rd_en;
    reg [7:0] din;
    wire [7:0] dout;
    wire      empty;
    wire      full;

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

    always #5 clk = ~clk;

    initial begin
        clk   = 1'b0;
        rst   = 1'b1;
        wr_en = 1'b0;
        rd_en = 1'b0;
        din   = 8'h00;

        #20;
        rst = 1'b0;

        // Veri yazma
        @(posedge clk);
        wr_en = 1'b1; din = 8'h11;
        @(posedge clk);
        din = 8'h22;
        @(posedge clk);
        wr_en = 1'b0;

        #20;

        // Veri okuma
        @(posedge clk);
        rd_en = 1'b1;
        @(posedge clk);
        @(posedge clk);
        rd_en = 1'b0;

        #40;
        $finish;
    end

    initial begin
        $monitor("Zaman = %0t ns | wr = %b | rd = %b | din = %h | dout = %h | empty = %b | full = %b", 
                 $time, wr_en, rd_en, din, dout, empty, full);
    end

endmodule