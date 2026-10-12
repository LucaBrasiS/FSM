`timescale 1ns / 1ps

module FIFO (
    input  logic       clk,
    input  logic       rst,
    input  logic       wr_en,
    input  logic       rd_en,
    input  logic [7:0] din,
    output logic [7:0] dout,
    output logic       empty,
    output logic       full
);

    // 8 derinlikli, 8-bit genişliğinde bellek dizisi
    logic [7:0] bellek [7:0];
    
    logic [2:0] yaz_ptr;
    logic [2:0] oku_ptr;
    logic [3:0] data_cnt;
    
    // Boş ve dolu bayrakları (Flags)
    assign empty = (data_cnt == 4'd0);
    assign full  = (data_cnt == 4'd8);
    
    // Sıralı Bellek Yönetimi (Sequential Logic)
    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            yaz_ptr  <= 3'd0;
            oku_ptr  <= 3'd0;
            data_cnt <= 4'd0;
            dout     <= 8'd0;
        end else begin
            // 1. Sadece Yazma Durumu
            if (wr_en && !full && !(rd_en && !empty)) begin
                bellek[yaz_ptr] <= din;
                yaz_ptr         <= yaz_ptr + 1'b1;
                data_cnt        <= data_cnt + 1'b1;
            end
            
            // 2. Sadece Okuma Durumu
            else if (rd_en && !empty && !(wr_en && !full)) begin
                dout            <= bellek[oku_ptr];
                oku_ptr         <= oku_ptr + 1'b1;
                data_cnt        <= data_cnt - 1'b1;
            end
            
            // 3. Aynı Anda Hem Okuma Hem Yazma Durumu
            else if ((wr_en && !full) && (rd_en && !empty)) begin
                bellek[yaz_ptr] <= din;
                dout            <= bellek[oku_ptr];
                yaz_ptr         <= yaz_ptr + 1'b1;
                oku_ptr         <= oku_ptr + 1'b1;
                // data_cnt değişmez (+1 ve -1 birbirini götürür)
            end
        end
    end

endmodule