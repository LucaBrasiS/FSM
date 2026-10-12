`timescale 1ns / 1ps

module FIFO (
    input wire       clk,
    input wire       rst,
    input wire       wr_en,
    input wire       rd_en,
    input wire [7:0] din,
    output reg [7:0] dout,
    output wire      empty,
    output wire      full
);
    
    reg [7:0] bellek [7:0];
    
    reg [2:0] yaz_ptr;
    reg [2:0] oku_ptr;
    reg [3:0] data_cnt;
    
    assign empty = (data_cnt == 4'd0);
    assign full  = (data_cnt == 4'd8);
    
    always @(posedge clk) begin
        if (rst) begin
            yaz_ptr  <= 3'd0;
            oku_ptr  <= 3'd0;
            data_cnt <= 4'd0;
            dout     <= 8'd0;
        end else begin
            if (wr_en && !full && !(rd_en && !empty)) begin
                bellek[yaz_ptr] <= din;
                yaz_ptr         <= yaz_ptr + 1'b1;
                data_cnt        <= data_cnt + 1'b1;
            end
            
            else if (rd_en && !empty && !(wr_en && !full)) begin
                dout            <= bellek[oku_ptr];
                oku_ptr         <= oku_ptr + 1'b1;
                data_cnt        <= data_cnt - 1'b1;
            end
            
            else if ((wr_en && !full) && (rd_en && !empty)) begin
                bellek[yaz_ptr] <= din;
                dout            <= bellek[oku_ptr];
                yaz_ptr         <= yaz_ptr + 1'b1;
                oku_ptr         <= oku_ptr + 1'b1;
            end
        end
    end
endmodule